SOLUTION_FILE = 'python_basics.py'

import unittest
from tempfile import TemporaryDirectory
from pathlib import Path
from python_basics import import_names
import json
import python_basics as task

class Examples(unittest.TestCase):
    def test_example_1(self):
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "names.json"
            path.write_text('["Аня", "Аня", "Илья"]', encoding="utf-8")
            self.assertEqual(import_names(path), ["Аня", "Аня", "Илья"])

class B03_6(unittest.TestCase):
    def test_successful_import(self):
        for names in [[], ["Женя", "Аня", "Женя"]]:
            with self.subTest(names=names), TemporaryDirectory() as folder:
                path = Path(folder) / "names.json"
                path.write_text(json.dumps(names, ensure_ascii=False), encoding="utf-8")
                self.assertEqual(task.import_names(path), names)

    def test_read_and_syntax_errors_keep_causes(self):
        for data, cause in [(None, FileNotFoundError), (b"\xff", UnicodeDecodeError), (b"[", json.JSONDecodeError)]:
            with self.subTest(cause=cause), TemporaryDirectory() as folder:
                path = Path(folder) / "incoming.json"
                if data is not None:
                    path.write_bytes(data)
                with self.assertRaises(task.DataImportError) as caught:
                    task.import_names(path)
                self.assertIsInstance(caught.exception.__cause__, cause)

    def test_valid_json_with_invalid_shape(self):
        for text in ['{"names":[]}', '"single"', '["ok",4]']:
            with self.subTest(text=text), TemporaryDirectory() as folder:
                path = Path(folder) / "incoming.json"
                path.write_text(text, encoding="utf-8")
                with self.assertRaises(task.SchemaError):
                    task.import_names(path)
