SOLUTION_FILE = 'solution.py'

import unittest
from solution import section_depth

class Examples(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(section_depth(*([[None, None], [0, 2], [None, 3], [None, None]], 1)), 3)

class P_TREE_DEPTH(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(section_depth(*([[None, None], [0, 2], [None, 3], [None, None]], 1)), 3)
    def test_case_2(self):
        self.assertEqual(section_depth(*([], None)), 0)
    def test_case_3(self):
        self.assertEqual(section_depth(*([[None, None]], 0)), 1)
    def test_case_4(self):
        self.assertEqual(section_depth(*([[None, None], [0, None], [1, None], [2, None]], 3)), 4)
    def test_case_5(self):
        self.assertEqual(section_depth(*([[1, 2], [None, None], [None, None]], 0)), 2)
