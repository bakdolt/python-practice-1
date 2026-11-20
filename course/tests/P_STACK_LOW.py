SOLUTION_FILE = 'solution.py'

import unittest
from solution import stack_readings

class Examples(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(stack_readings(*([['push', 8], ['push', 2], ['push', 5], ['min', None], ['top', None], ['pop', None], ['pop', None], ['min', None]],)), [2, 5, 8])

class P_STACK_LOW(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(stack_readings(*([['push', 8], ['push', 2], ['push', 5], ['min', None], ['top', None], ['pop', None], ['pop', None], ['min', None]],)), [2, 5, 8])
    def test_case_2(self):
        self.assertEqual(stack_readings(*([],)), [])
    def test_case_3(self):
        self.assertEqual(stack_readings(*([['pop', None], ['top', None], ['min', None]],)), [None, None])
    def test_case_4(self):
        self.assertEqual(stack_readings(*([['push', 0], ['push', -7], ['push', -7], ['pop', None], ['min', None], ['pop', None], ['min', None]],)), [-7, 0])
    def test_case_5(self):
        self.assertEqual(stack_readings(*([['push', 6], ['min', None], ['min', None], ['top', None]],)), [6, 6, 6])
