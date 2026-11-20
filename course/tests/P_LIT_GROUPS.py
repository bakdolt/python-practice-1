SOLUTION_FILE = 'solution.py'

import unittest
from solution import lit_groups

class Examples(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(lit_groups(*(['##..', '...#', '.#.#'],)), 3)

class P_LIT_GROUPS(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(lit_groups(*(['##..', '...#', '.#.#'],)), 3)
    def test_case_2(self):
        self.assertEqual(lit_groups(*([],)), 0)
    def test_case_3(self):
        self.assertEqual(lit_groups(*(['', ''],)), 0)
    def test_case_4(self):
        self.assertEqual(lit_groups(*(['..', '..'],)), 0)
    def test_case_5(self):
        self.assertEqual(lit_groups(*(['#.', '.#'],)), 2)
    def test_case_6(self):
        self.assertEqual(lit_groups(*(['#.#', '###', '#.#'],)), 1)
    def test_case_7(self):
        self.assertEqual(lit_groups(*(['#..##.#'],)), 3)
