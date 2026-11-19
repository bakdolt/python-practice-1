SOLUTION_FILE = 'algo_linear.py'

import unittest
from algo_linear import mirror_error
import algo_linear as tasks

class Examples(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(mirror_error("!A-2/3a"), (3, 5))

class A02_2(unittest.TestCase):
    def test_raw_label_indices(self):
        cases = [
            ("", None),
            ("-?!", None),
            ("/U4-u", None),
            ("0/rR:0", None),
            ("low-----X", (0, 8)),
            ("@K-x/5:k?", (3, 5)),
            ("!!01", (2, 3)),
        ]
        for label, expected in cases:
            with self.subTest(label=label):
                self.assertEqual(tasks.mirror_error(label), expected)
