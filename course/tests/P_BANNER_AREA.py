SOLUTION_FILE = 'solution.py'

import unittest
from solution import banner_area

class Examples(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(banner_area(*([3, 11, 2, 8],)), 16)

class P_BANNER_AREA(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(banner_area(*([3, 11, 2, 8],)), 16)
    def test_case_2(self):
        self.assertEqual(banner_area(*([],)), 0)
    def test_case_3(self):
        self.assertEqual(banner_area(*([15],)), 0)
    def test_case_4(self):
        self.assertEqual(banner_area(*([0, 0, 0],)), 0)
    def test_case_5(self):
        self.assertEqual(banner_area(*([4, 4, 4, 4, 4],)), 16)
    def test_case_6(self):
        self.assertEqual(banner_area(*([9, 2, 1, 9],)), 27)
    def test_case_7(self):
        self.assertEqual(banner_area(*([0, 5, 6, 0],)), 5)
