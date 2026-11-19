SOLUTION_FILE = 'python_basics.py'

import unittest
from python_basics import queue_name
import json
import python_basics as task

class Examples(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(queue_name('{"queue":"печать","priority":2}'), "печать")

class B03_3(unittest.TestCase):
    def test_value(self):
        self.assertEqual(task.queue_name('{"queue":"сборка","other":7}'), "сборка")
        self.assertEqual(task.queue_name('{"queue":""}'), "")

    def test_invalid_json_keeps_cause(self):
        with self.assertRaises(task.PayloadSyntaxError) as caught:
            task.queue_name('{"queue":')
        self.assertIsInstance(caught.exception.__cause__, json.JSONDecodeError)

    def test_invalid_schema(self):
        for text in ["[]", "{}", '{"queue":12}', '{"queue":null}']:
            with self.subTest(text=text), self.assertRaises(task.SchemaError):
                task.queue_name(text)
