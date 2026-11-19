SOLUTION_FILE = 'python_basics.py'

import unittest
from python_basics import read_user_id
import python_basics as task

class Examples(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(read_user_id({"user": {"id": 3, "name": "Лина"}}), 3)

class B03_4(unittest.TestCase):
    def test_positive_integer(self):
        result = task.read_user_id({"user": {"id": 1, "name": "Нина"}, "meta": None})
        self.assertIs(type(result), int)
        self.assertEqual(result, 1)

    def test_shape(self):
        for payload in [None, [], {}, {"user": []}, {"user": {}}]:
            with self.subTest(payload=payload), self.assertRaises(task.SchemaError):
                task.read_user_id(payload)

    def test_id_type_and_range(self):
        for value in [True, False, "3", 2.0, -4, 0, None]:
            with self.subTest(value=value), self.assertRaises(task.SchemaError) as caught:
                task.read_user_id({"user": {"id": value}})
            self.assertIn("user.id", str(caught.exception))
