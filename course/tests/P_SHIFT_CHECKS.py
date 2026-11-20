SOLUTION_FILE = 'solution.py'

import unittest
from solution import shift_labels

class Examples(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(shift_labels(*(5,)), ['1', 'вес', '3', 'вес', 'цвет'])

class P_SHIFT_CHECKS(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(shift_labels(*(5,)), ['1', 'вес', '3', 'вес', 'цвет'])
    def test_case_2(self):
        self.assertEqual(shift_labels(*(0,)), [])
    def test_case_3(self):
        self.assertEqual(shift_labels(*(1,)), ['1'])
    def test_case_4(self):
        self.assertEqual(shift_labels(*(2,)), ['1', 'вес'])
    def test_case_5(self):
        self.assertEqual(shift_labels(*(11,)), ['1', 'вес', '3', 'вес', 'цвет', 'вес', '7', 'вес', '9', 'вес+цвет', '11'])
