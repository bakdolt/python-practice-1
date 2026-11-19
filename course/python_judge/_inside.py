import json
import os
from pathlib import Path
import sys
import tempfile
import traceback
import unittest


def short_error(text):
    return text.strip()[-1200:]


def check(name):
    suite = unittest.defaultTestLoader.loadTestsFromName(name)
    result = unittest.TestResult()
    suite.run(result)
    problems = result.errors + result.failures
    if problems:
        return False, short_error(problems[0][1])
    if result.testsRun != 1 or result.skipped or result.expectedFailures or result.unexpectedSuccesses:
        return False, "Проверка не была выполнена полностью."
    return True, ""


def main():
    payload = json.load(sys.stdin)

    with os.fdopen(os.dup(1), "w", encoding="utf-8") as report, open(os.devnull, "w") as sink:
        os.dup2(sink.fileno(), 1)
        os.dup2(sink.fileno(), 2)
        os.chdir(tempfile.mkdtemp(dir="/tmp"))
        sys.path.insert(0, os.getcwd())
        for relative, body in payload["files"].items():
            path = Path(relative)
            path.parent.mkdir(exist_ok=True, parents=True)
            path.write_text(body, encoding="utf-8")
        rows = []
        try:
            compile(payload["files"][payload["filename"]], payload["filename"], "exec")
        except (SyntaxError, ValueError) as exc:
            message = short_error("".join(traceback.format_exception_only(type(exc), exc)))
            rows = [{"name": n, "passed": False, "message": message} for n in payload["names"]]
        else:
            for name in payload["names"]:
                try:
                    passed, message = check(name)
                except BaseException as exc:
                    passed, message = False, short_error("".join(traceback.format_exception_only(type(exc), exc)))
                rows.append({"name": name, "passed": passed, "message": message})
        json.dump({"nonce": payload["nonce"], "details": rows}, report, ensure_ascii=False)
        report.flush()


main()
