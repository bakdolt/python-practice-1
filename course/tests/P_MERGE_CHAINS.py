SOLUTION_FILE = 'solution.py'

import unittest
from solution import merge_chains

def inspect_merge(left, right):
    a = _make_nodes(left)
    b = _make_nodes(right)
    original = {node: node.value for node in a + b}
    result = merge_chains(a[0] if a else None, b[0] if b else None)
    return _read_chain(result, original)

def _make_nodes(values):
    from solution import Node

    nodes = [Node(value) for value in values]
    for left, right in zip(nodes, nodes[1:]):
        left.next = right
    return nodes

def _read_chain(head, original):
    remaining = original.copy()
    result = []
    while head is not None:
        if head not in remaining:
            raise ValueError("Цепочка содержит новый или повторный узел")
        if head.value != remaining.pop(head):
            raise ValueError("Значение исходного узла изменилось")
        result.append(head.value)
        head = head.next
    if remaining:
        raise ValueError("Часть исходных узлов потеряна")
    return result

class Examples(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(inspect_merge(*([1, 5, 8], [-2, 5, 9])), [-2, 1, 5, 5, 8, 9])

class P_MERGE_CHAINS(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(inspect_merge(*([1, 5, 8], [-2, 5, 9])), [-2, 1, 5, 5, 8, 9])
    def test_case_2(self):
        self.assertEqual(inspect_merge(*([], [])), [])
    def test_case_3(self):
        self.assertEqual(inspect_merge(*([], [-8, 0])), [-8, 0])
    def test_case_4(self):
        self.assertEqual(inspect_merge(*([3, 8], [])), [3, 8])
    def test_case_5(self):
        self.assertEqual(inspect_merge(*([2, 2], [2, 2])), [2, 2, 2, 2])
    def test_case_6(self):
        self.assertEqual(inspect_merge(*([4], [-7, -5, -3])), [-7, -5, -3, 4])
