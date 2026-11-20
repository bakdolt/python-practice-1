SOLUTION_FILE = 'solution.py'

import unittest
from solution import score_cutoff

class Examples(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(score_cutoff(*([11, 8, 11, 2, 6], 3)), 8)

class P_SCORE_CUTOFF(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(score_cutoff(*([11, 8, 11, 2, 6], 3)), 8)
    def test_case_2(self):
        self.assertEqual(score_cutoff(*([-5, -7, -1], 1)), -1)
    def test_case_3(self):
        self.assertEqual(score_cutoff(*([6, 6, 6], 3)), 6)
    def test_case_4(self):
        self.assertEqual(score_cutoff(*([], 1)), None)
    def test_case_5(self):
        self.assertEqual(score_cutoff(*([4], 2)), None)
    def test_case_6(self):
        self.assertEqual(score_cutoff(*([8], 0)), None)
    def test_case_7(self):
        self.assertEqual(score_cutoff(*([-8, 0, 9], 3)), -8)
