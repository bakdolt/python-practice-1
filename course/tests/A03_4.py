SOLUTION_FILE = 'algo_linear.py'

import unittest
from algo_linear import batch_totals
import algo_linear as tasks

class Examples(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(batch_totals([0, 4, -2], [(1, 2), (2, 2)]), [-6, 0])

class A03_4(unittest.TestCase):
    def test_half_open_queries_in_input_order(self):
        for prefix, spans, expected in [
            ([0], [], []),
            ([0], [(0, 0)], [0]),
            ([0, -7], [(0, 1), (1, 1)], [-7, 0]),
            ([0, 7, 3, 12], [(1, 3), (0, 3), (1, 2), (0, 0), (1, 3)], [5, 12, -4, 0, 5]),
        ]:
            with self.subTest(prefix=prefix, spans=spans):
                self.assertEqual(tasks.batch_totals(prefix, spans), expected)

    def test_bounds(self):
        for invalid in [(-1, 1), (0, 4), (2, 1)]:
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                tasks.batch_totals([0, 3, -2, 8], [(0, 1), invalid])
