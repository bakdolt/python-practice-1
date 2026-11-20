SOLUTION_FILE = 'solution.py'

import unittest
from solution import allocate_lockers

class Examples(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(allocate_lockers(*({'S': 1, 'L': 2}, ['L', 'S', 'S', 'L', 'L'])), [True, True, False, True, False])

class P_LOCKERS(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(allocate_lockers(*({'S': 1, 'L': 2}, ['L', 'S', 'S', 'L', 'L'])), [True, True, False, True, False])
    def test_case_2(self):
        self.assertEqual(allocate_lockers(*({}, [])), [])
    def test_case_3(self):
        self.assertEqual(allocate_lockers(*({}, ['M'])), [False])
    def test_case_4(self):
        self.assertEqual(allocate_lockers(*({'низкая': 0, 'высокая': 1}, ['низкая', 'высокая'])), [False, True])
    def test_case_5(self):
        self.assertEqual(allocate_lockers(*({'A': 1}, ['B', 'A'])), [False, True])
