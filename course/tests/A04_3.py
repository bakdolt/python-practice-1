SOLUTION_FILE = 'algo_structures.py'

import unittest
from algo_structures import wait_for_lower
import algo_structures as tasks

class Examples(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(wait_for_lower([6, 6, 9, 4]), [3, 2, 1, 0])

class A04_3(unittest.TestCase):
    def test_equal_value_keeps_waiting(self):
        self.assertEqual(tasks.wait_for_lower([2, 2, 3, 1]), [3, 2, 1, 0])

    def test_nearest_match(self):
        self.assertEqual(tasks.wait_for_lower([4, 2, 6, 5, -1, -3]), [1, 3, 1, 1, 1, 0])

    def test_no_lower_reading(self):
        for values in ([], [2], [-3, -2, -2, 7]):
            with self.subTest(values=values):
                self.assertEqual(tasks.wait_for_lower(values), [0] * len(values))
