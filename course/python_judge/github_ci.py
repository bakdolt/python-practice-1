import json
import os
from pathlib import Path
import re
import subprocess
from uuid import UUID

from python_judge.public_tasks import get_task
from python_judge.run import MAX_SOURCE, run


def identify(worktree, sha):
    changes = subprocess.check_output(
        ["git", "diff", "--name-status", "--no-renames", "-z", f"{sha}^", sha, "--"],
        cwd=worktree, timeout=10,
    ).split(b"\0")
    if len(changes) != 3 or changes[0] != b"A" or changes[2]:
        raise ValueError("Expected one added submission")
    path = changes[1].decode("ascii")
    match = re.fullmatch(r"submissions/([A-Z0-9_]+)/(examples|submit)/([0-9a-f-]{36})\.py", path)
    if not match:
        raise ValueError("Unexpected submission path")
    key, mode, identifier = match.groups()
    if str(UUID(identifier)) != identifier:
        raise ValueError("Invalid submission identity")
    task = get_task(worktree / "course", key)
    return path, task, mode, identifier


def prepare():
    _, task, mode, identifier = identify(Path(os.environ["GITHUB_WORKSPACE"]), os.environ["GITHUB_SHA"])
    with Path(os.environ["GITHUB_OUTPUT"]).open("a", encoding="utf-8") as outputs:
        outputs.write(f"submission_id={identifier}\ntask={task.id}\nmode={mode}\ntotal={len(task.case_names(mode))}\n")


def run_submission(worktree, sha, run_id, attempt, checker=run):
    path, task, mode, identifier = identify(worktree, sha)
    source = worktree / path
    if source.is_symlink() or not source.is_file() or source.stat().st_size > MAX_SOURCE:
        raise ValueError("Invalid submission file")
    report = checker(task, source.read_bytes().decode("utf-8"), mode)
    return {"submission_id": identifier, "task": task.id, "mode": mode, "sha": sha,
            "run_id": int(run_id), "attempt": int(attempt), "report": report}


def main():
    sha = os.environ["GITHUB_SHA"]
    if not re.fullmatch("[0-9a-f]{40}", sha):
        raise ValueError("Invalid commit")
    result = run_submission(Path(os.environ["GITHUB_WORKSPACE"]), sha,
                            os.environ["GITHUB_RUN_ID"], os.environ["GITHUB_RUN_ATTEMPT"])
    (Path(os.environ["RUNNER_TEMP"]) / "python-result.json").write_text(
        json.dumps(result, ensure_ascii=False), encoding="utf-8"
    )
