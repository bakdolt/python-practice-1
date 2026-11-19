SOLUTION_FILE = 'python_support/report.py'

import unittest
from pathlib import Path
from python_support import report
import subprocess
import sys

class Examples(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(report.label(" daily "), "[DAILY]")

class B03_1(unittest.TestCase):
    def run_python(self, *args):
        return subprocess.run(
            [sys.executable, "-X", "utf8", *args],
            cwd=Path(__file__).resolve().parent,
            encoding="utf-8", capture_output=True, timeout=8, check=True,
        )

    def test_import_is_quiet(self):
        result = self.run_python("-c", "import python_support.report")
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr, "")

    def test_public_alias_is_provided_helper(self):
        from python_support import labels, report

        self.assertIs(report.label, labels.format_label)
        self.assertEqual(report.label(" ok "), "[OK]")

    def test_module_entry_point(self):
        result = self.run_python("-m", "python_support.report")
        self.assertEqual(result.stdout.splitlines(), ["[DEMO]"])
