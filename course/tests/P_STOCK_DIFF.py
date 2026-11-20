SOLUTION_FILE = 'solution.py'

import unittest
from solution import stock_diff

class Examples(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(stock_diff(*(['R', 'Q', 'R', 'A'], ['Y', 'Q', 'K'])), [['R', 'A'], ['Y', 'K']])

class P_STOCK_DIFF(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(stock_diff(*(['R', 'Q', 'R', 'A'], ['Y', 'Q', 'K'])), [['R', 'A'], ['Y', 'K']])
    def test_case_2(self):
        self.assertEqual(stock_diff(*([], [])), [[], []])
    def test_case_3(self):
        self.assertEqual(stock_diff(*(['А', 'А'], [])), [['А'], []])
    def test_case_4(self):
        self.assertEqual(stock_diff(*([], ['k', 'K', 'k'])), [[], ['k', 'K']])
    def test_case_5(self):
        self.assertEqual(stock_diff(*(['T', 'S', 'T'], ['S', 'T', 'T'])), [[], []])
