SOLUTION_FILE = 'solution.py'

import unittest
from solution import sensor_history

class Examples(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(sensor_history(*([[8, 0], [4, -2], [9, 6]],)), [[8, 4, 9], [0, -2, 6]])

class P_SENSOR_TABLE(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(sensor_history(*([[8, 0], [4, -2], [9, 6]],)), [[8, 4, 9], [0, -2, 6]])
    def test_case_2(self):
        self.assertEqual(sensor_history(*([],)), [])
    def test_case_3(self):
        self.assertEqual(sensor_history(*([[], []],)), [])
    def test_case_4(self):
        self.assertEqual(sensor_history(*([[2, -3, 0]],)), [[2], [-3], [0]])
    def test_case_5(self):
        self.assertEqual(sensor_history(*([[-4], [7]],)), [[-4, 7]])
