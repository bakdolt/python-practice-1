SOLUTION_FILE = 'algo_structures.py'

import unittest
from algo_structures import nearest_readings
from collections import Counter
import algo_structures as tasks

class Examples(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(sorted(nearest_readings(iter([4, 9, 13, 11]), 10, 2)), [9, 11])

class A07_1(unittest.TestCase):
    def check_selection(self, values, target, k):
        selected = tasks.nearest_readings(iter(values), target, k)
        self.assertIsInstance(selected, list)
        self.assertEqual(len(selected), min(k, len(values)))
        self.assertFalse(Counter(selected) - Counter(values), "Некоторое значение выбрано чаще, чем встречалось")
        expected_distances = sorted(abs(value - target) for value in values)[:k]
        self.assertEqual(sorted(abs(value - target) for value in selected), expected_distances)

    def test_equidistant_candidates(self):
        self.check_selection([-3, 3, 1, 9, -1], 0, 3)

    def test_distance_relative_to_target_with_multiplicity(self):
        self.check_selection([8, 16, -1, 22, 14, 16, 0], 15, 4)

    def test_empty_zero_and_oversized(self):
        self.check_selection([], 3, 5)
        self.check_selection([2, 2, 2], 2, 0)
        self.check_selection([2, -2, 2], 1, 5)
