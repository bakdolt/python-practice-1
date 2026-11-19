SOLUTION_FILE = 'algo_linear.py'

import unittest
from algo_linear import adjacent_totals
import algo_linear as tasks

class Examples(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(adjacent_totals([6, -3, 8]), [3, 5])

class A03_1(unittest.TestCase):
    def test_contiguous_intervals(self):
        for changes, expected in [
            ([], []),
            ([-6], []),
            ([7, -7], [0]),
            ([8, -4, 9, 0], [4, 5, 9]),
            ([5, 5, 5], [10, 10]),
        ]:
            with self.subTest(changes=changes):
                self.assertEqual(tasks.adjacent_totals(changes), expected)
