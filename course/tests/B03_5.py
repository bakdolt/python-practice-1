SOLUTION_FILE = 'python_basics.py'

import unittest
from python_basics import RunLog
from dataclasses import is_dataclass
import python_basics as task

class Examples(unittest.TestCase):
    def test_example_1(self):
        log = RunLog("импорт")
        log.record("старт")
        self.assertEqual(log.messages, ["старт"])

class B03_5(unittest.TestCase):
    def test_constructor(self):
        self.assertTrue(is_dataclass(task.RunLog))
        log = task.RunLog("обучение")
        self.assertEqual(log.name, "обучение")
        self.assertEqual(log.messages, [])

    def test_order_and_repeated_events(self):
        log = task.RunLog("проверка")
        for message in ["старт", "старт", "готово"]:
            log.record(message)
        self.assertEqual(log.messages, ["старт", "старт", "готово"])

    def test_independent_instances(self):
        first, second = task.RunLog("a"), task.RunLog("b")
        first.record("ошибка")
        self.assertEqual(first.messages, ["ошибка"])
        self.assertEqual(second.messages, [])
        self.assertIsNot(first.messages, second.messages)
