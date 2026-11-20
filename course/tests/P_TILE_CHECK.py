SOLUTION_FILE = 'solution.py'

import unittest
from solution import same_tiles

class Examples(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(same_tiles(*('касса', 'сакса')), True)

class P_TILE_CHECK(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(same_tiles(*('касса', 'сакса')), True)
    def test_case_2(self):
        self.assertEqual(same_tiles(*('', '')), True)
    def test_case_3(self):
        self.assertEqual(same_tiles(*('ппк', 'пкк')), False)
    def test_case_4(self):
        self.assertEqual(same_tiles(*('а', 'А')), False)
    def test_case_5(self):
        self.assertEqual(same_tiles(*('x ', 'x')), False)
    def test_case_6(self):
        self.assertEqual(same_tiles(*('!a!', 'a!!')), True)
