SOLUTION_FILE = 'solution.py'

import unittest
from solution import print_tag

class Examples(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(print_tag(*('зал.2.А',)), 'зал(точка)2(точка)А')

class P_PRINT_TAG(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(print_tag(*('зал.2.А',)), 'зал(точка)2(точка)А')
    def test_case_2(self):
        self.assertEqual(print_tag(*('',)), '')
    def test_case_3(self):
        self.assertEqual(print_tag(*('rack-5',)), 'rack-5')
    def test_case_4(self):
        self.assertEqual(print_tag(*('.x.',)), '(точка)x(точка)')
    def test_case_5(self):
        self.assertEqual(print_tag(*(' . .',)), ' (точка) (точка)')
    def test_case_6(self):
        self.assertEqual(print_tag(*('a..z',)), 'a(точка)(точка)z')
