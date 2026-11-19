SOLUTION_FILE = 'algo_structures.py'

import unittest
from algo_structures import open_routes
import algo_structures as tasks

class Examples(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(open_routes(4, {1}), 2)

class A08_2(unittest.TestCase):
    def test_start_and_first_jump(self):
        self.assertEqual(tasks.open_routes(0, set()), 1)
        self.assertEqual(tasks.open_routes(1, {1}), 0)
        self.assertEqual(tasks.open_routes(2, {1}), 1)

    def test_route_around_closure(self):
        self.assertEqual(tasks.open_routes(5, {2}), 2)
        self.assertEqual(tasks.open_routes(5, set()), 8)

    def test_unreachable(self):
        self.assertEqual(tasks.open_routes(6, {2, 3}), 0)
        self.assertEqual(tasks.open_routes(4, {4}), 0)
