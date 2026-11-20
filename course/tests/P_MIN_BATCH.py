SOLUTION_FILE = 'solution.py'

import unittest
from solution import shortest_batch

class Examples(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(shortest_batch(*([3, 1, 8, 2, 7], 9)), 2)

class P_MIN_BATCH(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(shortest_batch(*([3, 1, 8, 2, 7], 9)), 2)
    def test_case_2(self):
        self.assertEqual(shortest_batch(*([], 4)), 0)
    def test_case_3(self):
        self.assertEqual(shortest_batch(*([0, 0, 0], 1)), 0)
    def test_case_4(self):
        self.assertEqual(shortest_batch(*([0, 0, 2, 2, 15], 15)), 1)
    def test_case_5(self):
        self.assertEqual(shortest_batch(*([6, 1, 6], 12)), 3)
    def test_case_6(self):
        self.assertEqual(shortest_batch(*([4, 2, 0], 7)), 0)
    def test_case_7(self):
        self.assertEqual(shortest_batch(*([0, 3, 0, 6], 9)), 3)
