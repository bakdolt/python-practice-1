SOLUTION_FILE = 'algo_structures.py'

import unittest
from algo_structures import rotated_index
import algo_structures as tasks

class Examples(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(rotated_index([12, 15, 1, 3, 8], 3), 3)

class A05_2(unittest.TestCase):
    def test_both_sides_of_pivot(self):
        builds = [11, 13, 20, 23, -4, 0, 3, 8]
        for index, wanted in enumerate(builds):
            with self.subTest(wanted=wanted):
                self.assertEqual(tasks.rotated_index(builds, wanted), index)

    def test_without_rotation_and_singleton(self):
        self.assertEqual(tasks.rotated_index([4, 9, 21], 21), 2)
        self.assertEqual(tasks.rotated_index([6], 6), 0)

    def test_missing(self):
        for builds, wanted in [([], 0), ([2, 1], 3), ([7], 5), ([20, 25, 3, 9, 12], 10)]:
            with self.subTest(builds=builds, wanted=wanted):
                self.assertIsNone(tasks.rotated_index(builds, wanted))
