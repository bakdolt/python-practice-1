import ast
from dataclasses import dataclass
from pathlib import Path
import re


@dataclass
class TestTask:
    id: str
    filename: str
    source: str
    methods: dict
    support: dict

    def files(self, mode):
        module = "examples.py" if mode == "examples" else "checks.py"
        return {module: self.source, **self.support}

    def case_names(self, mode):
        return self.methods[mode]


def get_task(course: Path, key: str):
    if not re.fullmatch(r"[A-Z0-9_]+", key):
        raise ValueError("Invalid exercise")
    path = course / "tests" / (key + ".py")
    if not path.is_file():
        raise ValueError("Unknown exercise")
    source = path.read_text(encoding="utf-8")
    statements = ast.parse(source, filename=path.name).body
    filename = ast.literal_eval(statements[0].value)
    methods = {}
    for mode, module, class_name in (("examples", "examples", "Examples"), ("submit", "checks", key)):
        suite = next(n for n in statements if isinstance(n, ast.ClassDef) and n.name == class_name)
        methods[mode] = tuple(f"{module}.{class_name}.{n.name}" for n in suite.body
                              if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name.startswith("test_"))
    support = {}
    if key == "B03_1":
        support["python_support/labels.py"] = (course / "python_support/labels.py").read_text(encoding="utf-8")
    return TestTask(key, filename, source, methods, support)
