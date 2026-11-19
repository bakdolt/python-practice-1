SOLUTION_FILE = 'python_basics.py'

import unittest
from python_basics import route_with_stop
import python_basics as task

class Examples(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(route_with_stop("Парк", ["Вокзал"]), ["Вокзал", "Парк"])

class B02_3(unittest.TestCase):
    def test_default_is_fresh(self):
        first = task.route_with_stop("А")
        second = task.route_with_stop("Б")
        self.assertEqual(first, ["А"])
        self.assertEqual(second, ["Б"])

    def test_supplied_list_survives_later_edits(self):
        route = ["Б", "А"]
        result = task.route_with_stop("А", route)
        self.assertEqual(result, ["Б", "А", "А"])
        result.append("В")
        self.assertEqual(route, ["Б", "А"])

    def test_empty_supplied_list(self):
        route = []
        self.assertEqual(task.route_with_stop("В", route), ["В"])
        self.assertEqual(route, [])
