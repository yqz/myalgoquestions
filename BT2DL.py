#!/usr/bin/python

"""
QUESTION: convert a binary tree to a doubly linked list using the left,right pointer
of tree. The order should be a in-order traversal. """

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.left = left 
        self.right = right
        self.data = data 
    def __getattr__(self, key):
        if key == 'next':
            return self.right
        elif key == 'prev':
            return self.left
        else:
            raise AttributeError()


def _BT2DL(root):
    """ Convert a binary tree to doubly linked list.
    return the head and the tail of the linked list."""
    lhead=ltail=rhead=rtail=None
    if root.left is not None:
        lhead, ltail = _BT2DL(root.left)
    if root.right is not None:
        rhead, rtail = _BT2DL(root.right)

    if ltail is not None:
        assert ltail.next is None
        root.prev = ltail
        ltail.next = root
    if rhead is not None:
        assert rhead.prev is None
        root.next = rhead
        rhead.prev = root
    return lhead or root, rtail or root 

def BT2DL(root):
    if root is None:
        return None
    else:
        return _BT2DL(root)[0]


import unittest

class MyUnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def ll2array(self, head):
        result = []
        while head:
            if head.next:
                self.assertEqual(head, head.next.prev)
            result.append(head.data)
            head = head.next
        return result



    def test_func(self):
        root = Node(1, Node(2), Node(3))
        self.assertEqual([2,1,3], self.ll2array(BT2DL(root)))
        root = Node(1, Node(2,Node(3)), Node(4, None, Node(5)))
        self.assertEqual([3,2,1,4,5], self.ll2array(BT2DL(root)))
        root = Node(1, Node(2,None, Node(3)), Node(4, Node(5)))
        self.assertEqual([2,3,1,5,4], self.ll2array(BT2DL(root)))


if __name__ == '__main__':
    unittest.main()



