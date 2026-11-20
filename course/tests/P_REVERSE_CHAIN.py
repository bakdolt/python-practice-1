SOLUTION_FILE = 'solution.py'

import unittest
from solution import reverse_chain

def inspect_reversal(values):
    nodes = _make_nodes(values)
    original = {node: node.value for node in nodes}
    result = reverse_chain(nodes[0] if nodes else None)
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
        self.assertEqual(inspect_reversal(*([9, -2, 6],)), [6, -2, 9])

class P_REVERSE_CHAIN(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(inspect_reversal(*([9, -2, 6],)), [6, -2, 9])
    def test_case_2(self):
        self.assertEqual(inspect_reversal(*([],)), [])
    def test_case_3(self):
        self.assertEqual(inspect_reversal(*([4],)), [4])
    def test_case_4(self):
        self.assertEqual(inspect_reversal(*([5, 5, 8, -3],)), [-3, 8, 5, 5])
    def test_case_5(self):
        self.assertEqual(inspect_reversal(*([0, 12],)), [12, 0])
