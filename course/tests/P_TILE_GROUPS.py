SOLUTION_FILE = 'solution.py'

import unittest
from solution import tile_groups

class Examples(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(tile_groups(*(['лес', 'сад', 'сел', 'сада', 'дса'],)), [['лес', 'сел'], ['сад', 'дса'], ['сада']])

class P_TILE_GROUPS(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(tile_groups(*(['лес', 'сад', 'сел', 'сада', 'дса'],)), [['лес', 'сел'], ['сад', 'дса'], ['сада']])
    def test_case_2(self):
        self.assertEqual(tile_groups(*([],)), [])
    def test_case_3(self):
        self.assertEqual(tile_groups(*(['', 'a', ''],)), [['', ''], ['a']])
    def test_case_4(self):
        self.assertEqual(tile_groups(*(['аа', 'а', 'аа'],)), [['аа', 'аа'], ['а']])
    def test_case_5(self):
        self.assertEqual(tile_groups(*(['Ab', 'bA', 'ab'],)), [['Ab', 'bA'], ['ab']])
