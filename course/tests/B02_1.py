SOLUTION_FILE = 'python_basics.py'

import unittest
from python_basics import total_units
import python_basics as task

class Examples(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(total_units(" 03", " 12 "), 36)
    def test_example_2(self):
        self.assertEqual(total_units("0", "5"), 0)

class B02_1(unittest.TestCase):
    def test_number_of_units(self):
        for boxes, per_box, expected in [(" 12 ", "3", 36), ("0", "42", 0), ("7", " 01 ", 7)]:
            with self.subTest(boxes=boxes, per_box=per_box):
                actual = task.total_units(boxes, per_box)
                self.assertIs(type(actual), int)
                self.assertEqual(actual, expected)
