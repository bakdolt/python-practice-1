SOLUTION_FILE = 'solution.py'

import unittest
from solution import double_route

class Examples(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(double_route(*(['порт', 'парк'],)), ['порт', 'парк', 'порт', 'парк'])

class P_DOUBLE_PLAN(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(double_route(*(['порт', 'парк'],)), ['порт', 'парк', 'порт', 'парк'])
    def test_case_2(self):
        self.assertEqual(double_route(*([],)), [])
    def test_case_3(self):
        self.assertEqual(double_route(*(['лифт'],)), ['лифт', 'лифт'])
    def test_case_4(self):
        self.assertEqual(double_route(*(['x', 'x'],)), ['x', 'x', 'x', 'x'])
    def test_case_5(self):
        self.assertEqual(double_route(*(['C', 'A', 'C'],)), ['C', 'A', 'C', 'C', 'A', 'C'])
