SOLUTION_FILE = 'solution.py'

import unittest
from solution import has_loop

def inspect_route(values, loop_to):
    nodes = _make_nodes(values)
    if loop_to is not None:
        nodes[-1].next = nodes[loop_to]
    return has_loop(nodes[0] if nodes else None)

def _make_nodes(values):
    from solution import Node

    nodes = [Node(value) for value in values]
    for left, right in zip(nodes, nodes[1:]):
        left.next = right
    return nodes

class Examples(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(inspect_route(*([1, 7, 4, 9], 1)), True)

class P_CHAIN_LOOP(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(inspect_route(*([1, 7, 4, 9], 1)), True)
    def test_case_2(self):
        self.assertEqual(inspect_route(*([], None)), False)
    def test_case_3(self):
        self.assertEqual(inspect_route(*([5], None)), False)
    def test_case_4(self):
        self.assertEqual(inspect_route(*([5], 0)), True)
    def test_case_5(self):
        self.assertEqual(inspect_route(*([3, 3, 3, 3], None)), False)
    def test_case_6(self):
        self.assertEqual(inspect_route(*([-2, 4], 0)), True)
