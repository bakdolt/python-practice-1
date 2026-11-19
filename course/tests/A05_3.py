SOLUTION_FILE = 'algo_structures.py'

import unittest
from algo_structures import first_slot
from collections.abc import Sequence
import algo_structures as tasks

class Examples(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(first_slot([2, 7, 7, 10], 7), 1)

class A05_3(unittest.TestCase):
    def test_first_of_repeated_group(self):
        self.assertEqual(tasks.first_slot([0, 6, 6, 6, 12, 13], 6), 1)

    def test_gap_and_ends(self):
        for start, expected in [(1, 0), (5, 1), (11, 3), (12, 3), (20, 4)]:
            with self.subTest(start=start):
                self.assertEqual(tasks.first_slot([3, 7, 9, 12], start), expected)

    def test_empty(self):
        self.assertEqual(tasks.first_slot([], 99), 0)

    def test_logarithmic_number_of_slot_reads(self):
        class Schedule(Sequence):
            def __init__(self, size):
                self.size = size
                self.reads = 0

            def __len__(self):
                return self.size

            def __getitem__(self, index):
                if isinstance(index, slice):
                    return [self[i] for i in range(*index.indices(self.size))]
                if index < 0:
                    index += self.size
                if not 0 <= index < self.size:
                    raise IndexError(index)
                self.reads += 1
                if self.reads > 2 * self.size.bit_length() + 4:
                    raise AssertionError("Превышен бюджет чтений. Исключайте половину интервала за шаг.")
                return index // 4

        for start, expected in [(0, 0), (14_125, 56_500), (16_400, 65_536)]:
            with self.subTest(start=start):
                self.assertEqual(tasks.first_slot(Schedule(65_536), start), expected)
