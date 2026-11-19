SOLUTION_FILE = 'python_basics.py'

import unittest
from python_basics import distinct_frequencies
import python_basics as task

class Examples(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(distinct_frequencies([4, 4, 7]), True)
    def test_example_2(self):
        self.assertEqual(distinct_frequencies([4, 4, 7, 7]), False)

class B02_5(unittest.TestCase):
    def test_frequencies(self):
        cases = [
            ([], True),
            ([9], True),
            ([7, -2], False),
            ([0, -4, 0, 0, 2, -4], True),
            ([3, 8, 8, 0, 0, 1, 1, 1], False),
        ]
        for codes, expected in cases:
            with self.subTest(codes=codes):
                self.assertIs(task.distinct_frequencies(codes), expected)
