SOLUTION_FILE = 'solution.py'

import unittest
from solution import section_levels

class Examples(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(section_levels(*(['A', 'B', 'C', 'D'], [[None, None], [2, 0], [None, 3], [None, None]], 1)), [['B'], ['C', 'A'], ['D']])

class P_SECTION_LEVELS(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(section_levels(*(['A', 'B', 'C', 'D'], [[None, None], [2, 0], [None, 3], [None, None]], 1)), [['B'], ['C', 'A'], ['D']])
    def test_case_2(self):
        self.assertEqual(section_levels(*([], [], None)), [])
    def test_case_3(self):
        self.assertEqual(section_levels(*(['X'], [[None, None]], 0)), [['X']])
    def test_case_4(self):
        self.assertEqual(section_levels(*(['z', 'r', 'z'], [[None, None], [0, 2], [None, None]], 1)), [['r'], ['z', 'z']])
    def test_case_5(self):
        self.assertEqual(section_levels(*(['Q', 'L', 'R', 'a', 'b'], [[1, 2], [None, 4], [3, None], [None, None], [None, None]], 0)), [['Q'], ['L', 'R'], ['b', 'a']])
