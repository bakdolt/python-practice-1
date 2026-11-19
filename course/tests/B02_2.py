SOLUTION_FILE = 'python_basics.py'

import unittest
from python_basics import count_in_budget
import python_basics as task

class Examples(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(count_in_budget([3, 8, 4, -1, 1], 4), 2)

class B02_2(unittest.TestCase):
    def test_threshold_and_stop(self):
        cases = [
            ([], 3, 0),
            ([0, 5, 6, 5], 5, 3),
            ([-1, 0, 1], 3, 0),
            ([7, 1, -1, 2], 2, 1),
        ]
        for values, limit, expected in cases:
            with self.subTest(values=values, limit=limit):
                actual = task.count_in_budget(values, limit)
                self.assertIs(type(actual), int)
                self.assertEqual(actual, expected)
