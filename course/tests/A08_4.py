SOLUTION_FILE = 'algo_structures.py'

import unittest
from algo_structures import minimum_packs
import algo_structures as tasks

class Examples(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(minimum_packs([3, 7, 8], 14), 2)

class A08_4(unittest.TestCase):
    def test_greedy_trap(self):
        self.assertEqual(tasks.minimum_packs([1, 5, 8], 10), 2)

    def test_reuse_and_unordered_sizes(self):
        self.assertEqual(tasks.minimum_packs([9, 3], 12), 2)
        self.assertEqual(tasks.minimum_packs([5, 3, 5], 9), 3)

    def test_zero_and_impossible(self):
        self.assertEqual(tasks.minimum_packs([], 0), 0)
        self.assertIsNone(tasks.minimum_packs([], 2))
        self.assertIsNone(tasks.minimum_packs([4, 6], 9))
