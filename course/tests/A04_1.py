SOLUTION_FILE = 'algo_structures.py'

import unittest
from algo_structures import serve_queue
import algo_structures as tasks

class Examples(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(serve_queue([("add", "A"), ("urgent", "B"), ("take", "")]), ["B"])

class A04_1(unittest.TestCase):
    def test_fifo_order(self):
        events = [("add", "AB"), ("add", "AC"), ("take", ""), ("add", "AD"), ("take", "")]
        self.assertEqual(tasks.serve_queue(events), ["AB", "AC"])

    def test_urgent_goes_to_front(self):
        events = [("add", "q"), ("urgent", "x"), ("urgent", "y")] + [("take", "")] * 3
        self.assertEqual(tasks.serve_queue(events), ["y", "x", "q"])

    def test_empty_take_and_pending_jobs(self):
        for events in ([], [("take", "")], [("take", ""), ("add", "pending")]):
            with self.subTest(events=events):
                self.assertEqual(tasks.serve_queue(events), [])
