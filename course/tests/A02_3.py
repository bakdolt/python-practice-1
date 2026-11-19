SOLUTION_FILE = 'algo_linear.py'

import unittest
from algo_linear import rack_pair
import algo_linear as tasks

class Examples(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(rack_pair([1, 1, 6, 9], 2), (0, 1))

class A02_3(unittest.TestCase):
    def test_missing_pair(self):
        for weights, target in [([], 6), ([4], 8), ([-1, 4, 6], 8)]:
            with self.subTest(weights=weights, target=target):
                self.assertIsNone(tasks.rack_pair(weights, target))

    def test_any_valid_two_positions(self):
        for weights, target in [([-8, -5, 2, 9], -3), ([6, 6], 12), ([0, 1, 3, 5, 6], 6)]:
            with self.subTest(weights=weights, target=target):
                actual = tasks.rack_pair(weights, target)
                self.assertIsInstance(actual, tuple)
                self.assertEqual(len(actual), 2)
                i, j = actual
                self.assertIs(type(i), int)
                self.assertIs(type(j), int)
                self.assertTrue(0 <= i < j < len(weights), "Нужны два разных индекса в порядке возрастания")
                self.assertEqual(weights[i] + weights[j], target)
