#!/usr/bin/python
from stack_with_min import StackWithMin

class QueueWithMin(object):
    def __init__(self):
        self._push_stack = StackWithMin()
        self._pop_stack = StackWithMin()

    def push(self, x):
        self._push_stack.push(x)

    def pop(self):
        if len(self._pop_stack) == 0:
            self._push_to_pop()
        return self._pop_stack.pop()

    def _push_to_pop(self):
        assert len(self._pop_stack) == 0
        while len(self._push_stack) > 0:
            self._pop_stack.push(self._push_stack.pop())

    def min(self):
        m1 = self._push_stack.min()
        m2 = self._pop_stack.min()
        if m1 is None: 
            return m2
        if m2 is None:
            return m1
        return min(m1, m2)

import unittest

class MyUnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_func(self):
        q = QueueWithMin()
        q.push(1)
        q.push(2)
        q.push(4)
        q.push(3)
        self.assertEqual(1, q.min())
        self.assertEqual(1, q.pop())
        self.assertEqual(2, q.min())
        self.assertEqual(2, q.pop())
        self.assertEqual(3, q.min())
        self.assertEqual(4, q.pop())
        self.assertEqual(3, q.min())
        q.push(1)
        self.assertEqual(1, q.min())
        self.assertEqual(3, q.pop())


if __name__ == '__main__':
    unittest.main()

