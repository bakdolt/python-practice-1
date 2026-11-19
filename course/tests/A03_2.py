SOLUTION_FILE = 'algo_linear.py'

import unittest
from algo_linear import peak_start
import algo_linear as tasks

class Examples(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(peak_start([-6, 2, 4, -8], 2), 1)

class A03_2(unittest.TestCase):
    def test_earliest_winning_start(self):
        for changes, width, expected in [
            ([-9, -4, -2, -8], 2, 1),
            ([8, -3, 8, -3], 2, 0),
            ([1, 4, 7], 2, 1),
            ([-3, 2, 2, -7], 1, 1),
            ([4, -9], 2, 0),
        ]:
            with self.subTest(changes=changes, width=width):
                self.assertEqual(tasks.peak_start(changes, width), expected)

    def test_impossible_width(self):
        for changes, width in [([], 1), ([4], 2), ([3, 9], 0), ([7, 9], -2)]:
            with self.subTest(changes=changes, width=width), self.assertRaises(ValueError):
                tasks.peak_start(changes, width)
