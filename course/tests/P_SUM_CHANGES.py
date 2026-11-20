SOLUTION_FILE = 'solution.py'

import unittest
from solution import net_change

class Examples(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(net_change(*(17, -6)), 11)

class P_SUM_CHANGES(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(net_change(*(17, -6)), 11)
    def test_case_2(self):
        self.assertEqual(net_change(*(-4, -11)), -15)
    def test_case_3(self):
        self.assertEqual(net_change(*(0, 0)), 0)
    def test_case_4(self):
        self.assertEqual(net_change(*(-82, 82)), 0)
    def test_case_5(self):
        self.assertEqual(net_change(*(1002, 35)), 1037)
