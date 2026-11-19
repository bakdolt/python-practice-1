SOLUTION_FILE = 'algo_structures.py'

import unittest
from algo_structures import narrow_interval
import algo_structures as tasks

class Examples(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(narrow_interval([3, 8], 9, 1, 2), (2, 2))

class A05_4(unittest.TestCase):
    def test_matching_midpoint_remains_candidate(self):
        self.assertEqual(tasks.narrow_interval([2, 4, 5, 5, 8, 9], 5, 1, 5), (1, 3))

    def test_middle_below_target(self):
        self.assertEqual(tasks.narrow_interval([0, 1, 4, 7, 8, 12], 7, 0, 5), (3, 5))

    def test_last_candidate_always_shrinks(self):
        self.assertEqual(tasks.narrow_interval([2, 7, 9], 8, 1, 2), (2, 2))
        self.assertEqual(tasks.narrow_interval([2, 7, 9], 1, 0, 1), (0, 0))
