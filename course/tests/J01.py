SOLUTION_FILE = 'python_engineering.py'

import unittest
import asyncio
from python_engineering import fetch_batch

class Examples(unittest.TestCase):
    def test_example_1(self):
        async def длина_строкой(key):
            return str(len(key))
        self.assertEqual(asyncio.run(fetch_batch(["март", "май", "март"], длина_строкой, 2)), ["4", "3", "4"])

class J01(unittest.IsolatedAsyncioTestCase):
    async def test_empty_input(self):
        async def unexpected(key):
            self.fail(f"Лишний вызов fetch({key!r})")

        self.assertEqual(await fetch_batch([], unexpected, 2), [])

    async def test_processes_repeated_keys_as_distinct_requests(self):
        calls = []

        async def echo(key):
            calls.append(key)
            return key.upper()

        expected = ["раз", "два", "раз"]
        result = await fetch_batch(expected.copy(), echo, 1)
        self.assertEqual(result, ["РАЗ", "ДВА", "РАЗ"])
        self.assertCountEqual(calls, expected)

    async def test_parallel_requests_preserve_input_order(self):
        release_first = asyncio.Event()

        async def reversed_finish(key):
            if key == "первый":
                await release_first.wait()
            else:
                release_first.set()
            return key.upper()


        result = await asyncio.wait_for(
            fetch_batch(["первый", "второй"], reversed_finish, 2), timeout=3
        )
        self.assertEqual(result, ["ПЕРВЫЙ", "ВТОРОЙ"])

    async def test_respects_concurrency_limit(self):
        for limit in (1, 2, 3):
            with self.subTest(limit=limit):
                active = peak = 0
                calls = []

                async def observe(key):
                    nonlocal active, peak
                    calls.append(key)
                    active += 1
                    peak = max(peak, active)
                    try:
                        await asyncio.sleep(0)
                        return key
                    finally:
                        active -= 1

                keys = list("abcdefg")
                self.assertEqual(await fetch_batch(keys, observe, limit), keys)
                self.assertCountEqual(calls, keys)
                self.assertLessEqual(peak, limit)
                self.assertEqual(active, 0)
