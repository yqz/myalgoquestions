#!/usr/bin/python

"""
QUESTION: Implement a stack that has a revision history everytime we do
push or pop. We will query the stack states for a given revision
"""

class RevisionStack(object):
    class Node(object):
        def __init__(self, parent, data):
            self.data = data
            self.parent = parent

    def __init__(self):
        # Array holding or head for each revision.
        self._revision = [None]

    def _get_head(self):
        return self._revision[-1]

    def push(self, data):
        head = self._get_head()
        node = self.Node(head, data)
        self._revision.append(node)

    def pop(self):
        head = self._get_head()
        if head is None:
            raise Exception("Stack is already empty")
        self._revision.append(head.parent)
        return head.data

    def revision(self, x):
        result = []
        head = self._revision[x]
        while head is not None:
            result.append(head.data)
            head = head.parent
        result.reverse()
        return result
        

import unittest

class MyUnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_func(self):
        stack = RevisionStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual([1,2,3], stack.revision(3))
        self.assertEqual([1,2], stack.revision(2))
        self.assertEqual([1], stack.revision(1))
        self.assertEqual([], stack.revision(0))
        self.assertEqual(3, stack.pop())
        self.assertEqual([1,2], stack.revision(4))
        self.assertEqual([1,2,3], stack.revision(3))
        self.assertEqual([1,2], stack.revision(2))
        stack.push(4)
        self.assertEqual([1,2,4], stack.revision(5))
        self.assertEqual([1,2], stack.revision(4))
        self.assertEqual([1,2,3], stack.revision(3))
        


if __name__ == '__main__':
    unittest.main()


