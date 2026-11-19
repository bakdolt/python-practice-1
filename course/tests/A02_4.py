SOLUTION_FILE = 'algo_linear.py'

import unittest
from algo_linear import pack_readings
import algo_linear as tasks

class Examples(unittest.TestCase):
    def test_example_1(self):
        readings = [None, 0, None, -5]
        self.assertIsNone(pack_readings(readings))
        self.assertEqual(readings, [0, -5, None, None])

class A02_4(unittest.TestCase):
    def test_update_the_passed_list(self):
        for values, expected in [
            ([], []),
            ([None, None], [None, None]),
            ([0, -3], [0, -3]),
            ([None, 9, None, 0, -2, 9, None], [9, 0, -2, 9, None, None, None]),
            ([4, None, None, 1], [4, 1, None, None]),
        ]:
            with self.subTest(values=values):
                self.assertIsNone(tasks.pack_readings(values))
                self.assertEqual(values, expected)
