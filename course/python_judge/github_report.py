import json
import os
from pathlib import Path
import re
from urllib.error import HTTPError
from urllib.request import HTTPRedirectHandler, Request, build_opener
from uuid import UUID


MAX_RECEIPT = 128 * 1024


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def make_receipt(env):
    task, mode, identifier = env["TASK"], env["MODE"], env["SUBMISSION_ID"]
    sha = env["GITHUB_SHA"]
    if (not re.fullmatch(r"[A-Z0-9_]+", task) or mode not in ("examples", "submit")
            or str(UUID(identifier)) != identifier or not re.fullmatch(r"[0-9a-f]{40}", sha)):
        raise ValueError("Unexpected grading identity")
    identity = {"submission_id": identifier, "sha": sha, "task": task, "mode": mode,
                "run_id": int(env["GITHUB_RUN_ID"]), "attempt": int(env["GITHUB_RUN_ATTEMPT"])}
    total = int(env["EXPECTED_TOTAL"])
    if not 0 < total <= 128:
        raise ValueError("Unexpected test count")
    if env["CHECK_OUTCOME"] == "success":
        artifact = Path(env["RUNNER_TEMP"]) / "grade/python-result.json"
        if artifact.is_symlink() or not 0 < artifact.stat().st_size <= MAX_RECEIPT:
            raise ValueError("Invalid report")
        data = json.loads(artifact.read_bytes())
        if any(data.get(k) != v for k, v in identity.items()) or data["report"]["total"] != total:
            raise ValueError("Report does not belong to this submission")
        report = data["report"]
    else:
        report = {"status": "error", "message": "GitHub Actions не завершил проверку решения.",
                  "total": total, "passed": 0, "details": []}
    return {**identity, "report": report}


def publish(data, env):
    repository = env["GITHUB_REPOSITORY"]
    if not re.fullmatch(r"[\w.-]+/[\w.-]+", repository, re.ASCII):
        raise ValueError("Invalid repository")
    endpoint = f"https://api.github.com/repos/{repository}/check-runs"
    summary = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    if len(summary.encode("utf-8")) > 60 * 1024:
        for row in data["report"]["details"]:
            row["message"] = row["message"][:160]
        summary = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    if len(summary.encode("utf-8")) > 60 * 1024:
        raise ValueError("Check summary exceeds limit")
    report = data["report"]
    body = {
        "name": "Python verdict", "head_sha": data["sha"], "external_id": data["submission_id"],
        "details_url": f"https://github.com/{repository}/actions/runs/{data['run_id']}",
        "status": "completed", "conclusion": "success" if report["status"] == "passed" else "failure",
        "output": {"title": f"{report['passed']} / {report['total']}", "summary": summary},
    }
    headers = {"Authorization": "Bearer " + env["GH_TOKEN"], "Content-Type": "application/json",
               "Accept": "application/vnd.github+json", "User-Agent": "EdPlatform-CI"}
    request = Request(endpoint, method="POST", headers=headers, data=json.dumps(body).encode("utf-8"))
    try:
        with build_opener(NoRedirect()).open(request, timeout=15):
            pass
    except HTTPError as error:
        raise RuntimeError(f"Cannot record check: HTTP {error.code}") from None


if __name__ == "__main__":
    publish(make_receipt(os.environ), os.environ)
