from __future__ import annotations

import json
from pathlib import Path, PurePosixPath
import re
import secrets
import subprocess
import threading
import time
from typing import Protocol


class Task(Protocol):
    filename: str

    def files(self, mode: str) -> dict[str, str]: ...

    def case_names(self, mode: str) -> tuple[str, ...]: ...


IMAGE = "python:3.12-slim-bookworm"
MAX_SOURCE = 64 * 1024
MAX_REPORT = 256 * 1024
LABEL = "org.bakdolt.python-judge=1"
SLOTS = ("edplatform-python-judge-0", "edplatform-python-judge-1")
HARNESS = Path(__file__).with_name("_inside.py")


def result(status, message, total=0, rows=None):
    rows = rows or []
    return {"status": status, "message": message, "passed": sum(row["passed"] for row in rows),
            "total": total, "details": rows}


def docker(*args):
    return subprocess.run(["docker", *args], capture_output=True, timeout=12, check=False)


def remove_if_stale(slot):
    inspection = docker("inspect", "--type", "container", slot)
    if inspection.returncode:
        return False
    container = json.loads(inspection.stdout)[0]
    labels = container["Config"].get("Labels") or {}
    if (labels.get("org.bakdolt.python-judge") != "1" or
            time.time() - float(labels.get("org.bakdolt.created", "inf")) < 120):
        return False

    return docker("rm", "--force", container["Id"]).returncode == 0


def allocate(image):

    opts = ["--pull=never", "--interactive", "--label", LABEL, "--label", f"org.bakdolt.created={time.time()}",
            "--network=none", "--read-only", "--cap-drop=ALL", "--security-opt=no-new-privileges",
            "--user=65534:65534", "--pids-limit=32", "--cpus=0.5", "--memory=160m", "--memory-swap=160m",
            "--ulimit", "nofile=128:128", "--ulimit", "fsize=4194304:4194304", "--log-driver=none",
            "--init", "--ipc=none", "--workdir=/tmp", "--tmpfs", "/tmp:rw,nosuid,nodev,noexec,size=24m,mode=1777",
            image, "python", "-I", "-B", "-u", "-X", "utf8", "-c", HARNESS.read_text(encoding="utf-8")]
    for slot in SLOTS:
        created = docker("create", "--name", slot, *opts)
        if created.returncode and b"already in use" in created.stderr and remove_if_stale(slot):
            created = docker("create", "--name", slot, *opts)
        if created.returncode == 0:
            cid = created.stdout.decode("ascii").strip()
            if re.fullmatch("[0-9a-f]{64}", cid):
                return cid
            raise RuntimeError("Docker вернул неизвестный идентификатор контейнера.")
        if b"already in use" not in created.stderr:
            raise RuntimeError("Не удалось создать изолированный контейнер. Проверьте Docker и наличие образа Python.")
    raise RuntimeError("Сейчас все исполнители заняты. Отправьте решение ещё раз.")


def attached(container, payload, wall_seconds):
    proc = subprocess.Popen(["docker", "start", "--attach", "--interactive", container],
                            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    buffer = bytearray()
    overflow = threading.Event()

    def read():
        with proc.stdout as stream:
            while chunk := stream.read1(8192):
                if len(buffer) + len(chunk) > MAX_REPORT:
                    overflow.set()
                    proc.kill()
                    return
                buffer.extend(chunk)

    def write():
        try:
            with proc.stdin as stream:
                stream.write(payload)
        except OSError:
            pass

    reader = threading.Thread(target=read, daemon=True)
    writer = threading.Thread(target=write, daemon=True)
    reader.start()
    writer.start()
    try:
        proc.wait(timeout=wall_seconds)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait(timeout=3)
        raise
    finally:
        reader.join(timeout=2)
        writer.join(timeout=2)
    if overflow.is_set():
        return "overflow", b""
    if reader.is_alive() or writer.is_alive():
        raise RuntimeError("Не удалось завершить обмен с исполнителем.")
    return proc.returncode, bytes(buffer)


def run(task: Task, source: str, mode: str, *, image: str = IMAGE, wall_seconds: int = 12) -> dict:

    if mode not in {"examples", "submit"} or not 1 <= wall_seconds <= 30:
        raise ValueError("Некорректный режим или лимит времени.")
    if not isinstance(source, str) or len(source) > MAX_SOURCE:
        return result("failed", "Допустимый размер решения — до 64 КиБ.")
    try:
        if len(source.encode("utf-8")) > MAX_SOURCE:
            return result("failed", "Допустимый размер решения — до 64 КиБ.")
    except UnicodeEncodeError:
        return result("failed", "Решение должно содержать корректный текст UTF-8.")
    names = list(task.case_names(mode))
    if (not names or len(names) > 32 or len(names) != len(set(names)) or
            any(not re.fullmatch(r"[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)+\.test_\w+", name) for name in names)):
        return result("error", "Не удалось загрузить список тестов.")
    files = {**task.files(mode), task.filename: source}
    if any(not isinstance(body, str) or not re.fullmatch(r"[A-Za-z0-9_./-]+", key)
           or PurePosixPath(key).is_absolute() or ".." in PurePosixPath(key).parts for key, body in files.items()):
        return result("error", "Некорректный комплект файлов задачи.", len(names))
    nonce = secrets.token_urlsafe(24)
    payload = json.dumps({"names": names, "files": files, "filename": task.filename, "nonce": nonce},
                         ensure_ascii=False).encode("utf-8")
    container = None
    try:
        container = allocate(image)
        try:
            code, output = attached(container, payload, wall_seconds)
        except subprocess.TimeoutExpired:
            return result("timeout", "Превышено время проверки. Проверьте условие выхода из циклов.", len(names))
        if code == "overflow":
            return result("failed", "Превышен допустимый размер вывода.", len(names))
        if code != 0:
            state = docker("inspect", "--format", "{{json .State}}", container)
            if not state.returncode:
                info = json.loads(state.stdout)
                if info.get("OOMKilled"):
                    return result("failed", "Решение превысило лимит памяти.", len(names))
                if info.get("Status") == "exited" and not info.get("Error"):
                    return result("failed", "Программа завершилась до окончания проверки.", len(names))
            return result("error", "Не удалось запустить проверку в контейнере.", len(names))
        try:
            report = json.loads(output)
            rows = report["details"]
            valid = (report["nonce"] == nonce and isinstance(rows, list)
                     and [r["name"] for r in rows] == names
                     and all(type(r["passed"]) is bool and isinstance(r["message"], str)
                             and len(r["message"]) <= 1200 for r in rows))
        except (ValueError, KeyError, TypeError):
            valid = False
        if not valid:
            return result("failed", "Программа завершилась без полного отчёта тестов.", len(names))
        if all(r["passed"] for r in rows):
            return result("passed", "Все проверки пройдены.", len(names), rows)
        return result("failed", "Проверьте решение по результатам тестов.", len(names), rows)
    except (OSError, subprocess.SubprocessError, RuntimeError, ValueError) as exc:
        message = str(exc) if isinstance(exc, RuntimeError) else "Исполнитель сейчас недоступен."
        return result("error", message, len(names))
    finally:
        if container:
            try:
                docker("rm", "--force", container)
            except (OSError, subprocess.SubprocessError):
                pass
