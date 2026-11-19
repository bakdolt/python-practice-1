SOLUTION_FILE = 'algo_structures.py'

import unittest
from algo_structures import contains_build
import algo_structures as tasks

class Examples(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(contains_build([2, 8, 13], 8), True)

class A05_1(unittest.TestCase):
    def test_present_at_edges_and_inside(self):
        for target in (-8, 2, 13):
            with self.subTest(target=target):
                self.assertIs(tasks.contains_build([-8, -1, 2, 5, 13], target), True)

    def test_only_exact_match_counts(self):
        for target in (-3, 4, 11):
            with self.subTest(target=target):
                self.assertIs(tasks.contains_build([1, 5, 10], target), False)

    def test_empty_catalogue(self):
        self.assertIs(tasks.contains_build([], 0), False)
