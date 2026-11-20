SOLUTION_FILE = 'solution.py'

import unittest
from solution import later_gain

class Examples(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(later_gain(*([12, 4, 10, 3, 7],)), 6)

class P_LATER_GAIN(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(later_gain(*([12, 4, 10, 3, 7],)), 6)
    def test_case_2(self):
        self.assertEqual(later_gain(*([],)), 0)
    def test_case_3(self):
        self.assertEqual(later_gain(*([7],)), 0)
    def test_case_4(self):
        self.assertEqual(later_gain(*([19, 9, 9, 2],)), 0)
    def test_case_5(self):
        self.assertEqual(later_gain(*([11, 15, 0],)), 4)
    def test_case_6(self):
        self.assertEqual(later_gain(*([0, 6, 6, 12],)), 12)
