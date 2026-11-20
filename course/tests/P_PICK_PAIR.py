SOLUTION_FILE = 'solution.py'

import unittest
from solution import pick_pair

class Examples(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(pick_pair(*([7, 3, 5, 1], 8)), [1, 2])

class P_PICK_PAIR(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(pick_pair(*([7, 3, 5, 1], 8)), [1, 2])
    def test_case_2(self):
        self.assertEqual(pick_pair(*([], 5)), [])
    def test_case_3(self):
        self.assertEqual(pick_pair(*([4], 8)), [])
    def test_case_4(self):
        self.assertEqual(pick_pair(*([4, 4], 8)), [0, 1])
    def test_case_5(self):
        self.assertEqual(pick_pair(*([5, 5, 5, 1], 6)), [0, 3])
    def test_case_6(self):
        self.assertEqual(pick_pair(*([0, 9, 0], 0)), [0, 2])
    def test_case_7(self):
        self.assertEqual(pick_pair(*([1, 9, 8], 5)), [])
