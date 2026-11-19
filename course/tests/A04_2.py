SOLUTION_FILE = 'algo_structures.py'

import unittest
from algo_structures import bracket_fault
import algo_structures as tasks

class Examples(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(bracket_fault("[{]}"), 2)
    def test_example_2(self):
        self.assertEqual(bracket_fault("(()"), 3)

class A04_2(unittest.TestCase):
    def test_valid_groups(self):
        for text in ("", "[{}]()([])", "(([]))"):
            with self.subTest(text=text):
                self.assertIsNone(tasks.bracket_fault(text))

    def test_first_bad_closing_position(self):
        for text, index in [("](", 0), ("{}[(])", 4), ("()}}", 2)]:
            with self.subTest(text=text):
                self.assertEqual(tasks.bracket_fault(text), index)

    def test_open_at_end(self):
        self.assertEqual(tasks.bracket_fault("([]){["), 6)
