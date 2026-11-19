SOLUTION_FILE = 'python_basics.py'

import unittest
from python_basics import running_balance
import python_basics as task

class Examples(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(running_balance([8, -3, 0]), [8, 5, 5])

class B02_4(unittest.TestCase):
    def test_balances(self):
        for changes, expected in [
            ([], []), ([4], [4]), ([6, -8, 2, 0, 3], [6, -2, 0, 0, 3]),
        ]:
            with self.subTest(changes=changes):
                original = changes.copy()
                result = task.running_balance(changes)
                self.assertEqual(result, expected)
                self.assertIsNot(result, changes)
                self.assertEqual(changes, original)
