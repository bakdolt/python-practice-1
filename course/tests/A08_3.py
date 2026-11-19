SOLUTION_FILE = 'algo_structures.py'

import unittest
from algo_structures import jump_trace
import algo_structures as tasks

class Examples(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(jump_trace(3), [(1, 0), (1, 1), (2, 1)])

class A08_3(unittest.TestCase):
    def test_no_arrivals_to_log(self):
        self.assertEqual(tasks.jump_trace(0), [])

    def test_first_possible_jumps(self):
        self.assertEqual(tasks.jump_trace(1), [(1, 0)])
        self.assertEqual(tasks.jump_trace(2), [(1, 0), (1, 1)])

    def test_separate_contributions(self):
        self.assertEqual(tasks.jump_trace(5), [(1, 0), (1, 1), (2, 1), (3, 2), (5, 3)])
