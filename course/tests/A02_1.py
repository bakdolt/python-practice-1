SOLUTION_FILE = 'algo_linear.py'

import unittest
from algo_linear import meter_prefix
import algo_linear as tasks

class Examples(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(meter_prefix([8, -3, 1]), [0, 8, 5, 6])

class A02_1(unittest.TestCase):
    def test_readings_at_all_boundaries(self):
        for values, expected in [
            ([], [0]),
            ([-10], [0, -10]),
            ([7, -9, 0, 5], [0, 7, -2, -2, 3]),
            ([0, 0], [0, 0, 0]),
        ]:
            with self.subTest(values=values):
                initial = values.copy()
                self.assertEqual(tasks.meter_prefix(values), expected)
                self.assertEqual(values, initial, "Список изменений был изменён")
