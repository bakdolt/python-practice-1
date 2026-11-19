SOLUTION_FILE = 'python_basics.py'

import unittest
from python_basics import remove_code
import python_basics as task

class Examples(unittest.TestCase):
    def test_example_1(self):
        codes = [5, 2, 5]
        k = remove_code(codes, 5)
        self.assertEqual((k, codes[:k]), (1, [2]))

class B02_6(unittest.TestCase):
    def test_caller_sees_remaining_prefix(self):
        cases = [
            ([], 1, []),
            ([4, 4], 4, []),
            ([2, 0, 2], 9, [2, 0, 2]),
            ([4, 4, 1, 0, 4, 1, 3], 4, [1, 0, 1, 3]),
        ]
        for codes, obsolete, remaining in cases:
            with self.subTest(codes=codes, obsolete=obsolete):
                size = task.remove_code(codes, obsolete)
                self.assertIs(type(size), int)
                self.assertEqual(size, len(remaining))
                self.assertCountEqual(codes[:size], remaining)
