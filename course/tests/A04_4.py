SOLUTION_FILE = 'algo_structures.py'

import unittest
from algo_structures import cutoff_history
import algo_structures as tasks

class Examples(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(cutoff_history(iter([4, -1, 8, 8]), 2), [None, -1, 4, 8])

class A04_4(unittest.TestCase):
    def test_prefixes_and_tied_values(self):
        self.assertEqual(tasks.cutoff_history(iter([3, 3, -4, 7, 9]), 2), [None, 3, 3, 3, 7])

    def test_largest_so_far(self):
        self.assertEqual(tasks.cutoff_history(iter([-9, -15, -2, -6]), 1), [-9, -9, -2, -2])

    def test_short_stream(self):
        self.assertEqual(tasks.cutoff_history(iter([8, 7]), 3), [None, None])
        self.assertEqual(tasks.cutoff_history(iter([]), 1), [])
