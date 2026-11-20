SOLUTION_FILE = 'solution.py'

import unittest
from solution import frequent_flags

class Examples(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(frequent_flags(*(['b', 'a', 'c', 'a', 'b', 'd'], 3)), ['b', 'a', 'c'])

class P_COMMON_FLAGS(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(frequent_flags(*(['b', 'a', 'c', 'a', 'b', 'd'], 3)), ['b', 'a', 'c'])
    def test_case_2(self):
        self.assertEqual(frequent_flags(*([], 2)), [])
    def test_case_3(self):
        self.assertEqual(frequent_flags(*(['x', 'x'], 0)), [])
    def test_case_4(self):
        self.assertEqual(frequent_flags(*(['пуск', 'СТОП', 'СТОП', 'стоп'], 6)), ['СТОП', 'пуск', 'стоп'])
    def test_case_5(self):
        self.assertEqual(frequent_flags(*(['q', 'p', 's', 'p', 's', 's'], 1)), ['s'])
