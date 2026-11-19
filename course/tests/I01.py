SOLUTION_FILE = 'python_engineering.py'

import unittest
from python_engineering import check_normalizer

def normalize_label(raw):
    label = raw.strip().lower()
    if not label:
        raise ValueError("Пустая метка")
    return label

class Examples(unittest.TestCase):
    def test_example_1(self):
        def normalize(text):
            label = text.strip().lower()
            if not label:
                raise ValueError("Пустая метка")
            return label
        self.assertIsNone(check_normalizer(normalize))

class I01(unittest.TestCase):
    def test_accepts_valid_implementation(self):
        self.assertIsNone(check_normalizer(normalize_label))

    def test_accepts_another_valid_implementation(self):
        def normalize(raw):
            if raw == "" or raw.isspace():
                raise ValueError("Укажите метку")
            return raw.lower().lstrip().rstrip()

        self.assertIsNone(check_normalizer(normalize))

    def test_detects_missing_lowercase(self):
        def broken(raw):
            normalize_label(raw)
            return raw.strip()

        with self.assertRaises(AssertionError):
            check_normalizer(broken)

    def test_detects_missing_trim(self):
        def broken(raw):
            normalize_label(raw)
            return raw.lower()

        with self.assertRaises(AssertionError):
            check_normalizer(broken)

    def test_detects_whitespace_accepted(self):
        def broken(raw):
            if raw and raw.isspace():
                return ""
            return normalize_label(raw)

        with self.assertRaises(AssertionError):
            check_normalizer(broken)

    def test_detects_empty_string_accepted(self):
        def broken(raw):
            if raw == "":
                return ""
            return normalize_label(raw)

        with self.assertRaises(AssertionError):
            check_normalizer(broken)

    def test_detects_removal_of_inner_space(self):
        def broken(raw):
            return normalize_label(raw).replace(" ", "")

        with self.assertRaises(AssertionError):
            check_normalizer(broken)
