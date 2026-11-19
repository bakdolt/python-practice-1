SOLUTION_FILE = 'algo_linear.py'

import unittest
from algo_linear import first_replay
import algo_linear as tasks

class Examples(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(first_replay(["p", "q", "q", "p"]), (1, 2))

class A01_1(unittest.TestCase):
    def test_first_event_delivered_twice(self):
        cases = [
            ([], None),
            (["5", "51", "15"], None),
            (["n", "n"], (0, 1)),
            (["pc", "tablet", "net", "tablet", "pc"], (1, 3)),
            (["42", "4", "2", "42", "42"], (0, 3)),
        ]
        for events, expected in cases:
            with self.subTest(events=events):
                self.assertEqual(tasks.first_replay(events), expected)
