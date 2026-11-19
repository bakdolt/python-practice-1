SOLUTION_FILE = 'algo_structures.py'

import unittest
from algo_structures import hop_distances
import algo_structures as tasks

class Examples(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(hop_distances({"s":["m","f"], "m":["f"], "f":[], "u":[]}, "s"), {"s":0, "m":1, "f":1})

class A06_1(unittest.TestCase):
    def test_uses_shortest_route(self):
        graph = {"s": ["a", "b"], "a": ["x"], "x": ["z"], "b": ["z"], "z": ["q"], "q": []}
        self.assertEqual(tasks.hop_distances(graph, "s"), {"s": 0, "a": 1, "b": 1, "x": 2, "z": 2, "q": 3})

    def test_directed_cycle_and_repeated_edge(self):
        graph = {"r": ["r", "t", "t"], "t": ["u"], "u": ["r"], "v": ["r"]}
        self.assertEqual(tasks.hop_distances(graph, "r"), {"r": 0, "t": 1, "u": 2})

    def test_isolated_start(self):
        self.assertEqual(tasks.hop_distances({"left": ["right"], "right": []}, "right"), {"right": 0})
