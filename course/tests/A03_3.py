SOLUTION_FILE = 'algo_linear.py'

import unittest
from algo_linear import longest_distinct_route
import algo_linear as tasks

class Examples(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(longest_distinct_route(["лес", "порт", "лес", "рынок"]), 3)

class A03_3(unittest.TestCase):
    def test_longest_contiguous_route(self):
        for stops, expected in [
            ([], 0),
            (["гимназия"] * 4, 1),
            (["Речной", "речной", "Речной"], 2),
            (["лес", "дом", "порт", "порт", "лес"], 3),
            (["B", "T", "B", "H", "Z"], 4),
            (["A", "B", "B", "C", "C", "D"], 2),
            (["а", "б", "б", "а"], 2),
        ]:
            with self.subTest(stops=stops):
                self.assertEqual(tasks.longest_distinct_route(stops), expected)
