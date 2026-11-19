SOLUTION_FILE = 'python_basics.py'

import unittest
from tempfile import TemporaryDirectory
from pathlib import Path
from python_basics import read_note
import python_basics as task

class Examples(unittest.TestCase):
    def test_example_1(self):
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "note.txt"
            path.write_bytes("первая строка\n".encode("utf-8"))
            self.assertEqual(read_note(path), "первая строка\n")

class B03_2(unittest.TestCase):
    def test_file_contents(self):
        for body in ["", "  Заметка\nстрока 2\n", "конец"]:
            with self.subTest(body=body), TemporaryDirectory() as folder:
                path = Path(folder) / "моя заметка.txt"
                path.write_bytes(body.encode("utf-8"))
                self.assertEqual(task.read_note(path), body)
                self.assertEqual(path.read_bytes(), body.encode("utf-8"))

    def test_missing_file(self):
        with TemporaryDirectory() as folder:
            path = Path(folder) / "нет.txt"
            with self.assertRaises(FileNotFoundError):
                task.read_note(path)
            self.assertFalse(path.exists())

    def test_invalid_utf8(self):
        with TemporaryDirectory() as folder:
            path = Path(folder) / "raw.bin"
            path.write_bytes(b"\xff")
            with self.assertRaises(UnicodeDecodeError):
                task.read_note(path)
