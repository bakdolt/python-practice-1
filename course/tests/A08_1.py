SOLUTION_FILE = 'algo_structures.py'

import unittest
from algo_structures import line_layouts
import algo_structures as tasks

class Examples(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(line_layouts(4), 3)

class A08_1(unittest.TestCase):
    def test_empty_layout(self):
        self.assertEqual(tasks.line_layouts(0), 1)

    def test_first_large_tile(self):
        for size, expected in [(1, 1), (2, 1), (3, 2)]:
            with self.subTest(size=size):
                self.assertEqual(tasks.line_layouts(size), expected)

    def test_order_counts(self):
        self.assertEqual(tasks.line_layouts(4), 3)
        self.assertEqual(tasks.line_layouts(8), 13)
