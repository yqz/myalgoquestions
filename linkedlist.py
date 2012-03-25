#!/usr/bin/python

class Node(object):
    def __init__(self, data=None, next=None):
        self.next = next
        self.data = data

    def add(self, node):
        end = self
        while end.next is not None:
            end = end.next
        end.next = node

    def __iter__(self):
        node = self
        while node is not None:
            yield node.data
            node = node.next

def delete_node(head, data):
    if head is None:
        return
    if head.data == data:
        return head.next
    while head.next is not None:
        if head.next.data == data:
            head.next = head.next.next
            return head
        head = head.next
    return head

def reverse(head):
    if head is None:
        return head
    prev = None
    cur = head
    while cur is not None:
        n = cur.next
        cur.next = prev
        prev = cur
        cur = n
    return prev



import unittest

class MyUnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_func(self):
        head = Node(1)
        head.add(Node(2))
        head.add(Node(3))
        head.add(Node(4))
        head.add(Node(5))
        self.assertEqual([1,2,3,4,5], [x for x in head])
        delete_node(head, 3)
        self.assertEqual([1,2,4,5], [x for x in head])
        head = delete_node(head, 1)
        self.assertEqual([2,4,5], [x for x in head])
        head = reverse(head)
        self.assertEqual([5,4,2], [x for x in head])
        head = reverse(head)
        self.assertEqual([2,4,5], [x for x in head])
        head = delete_node(head, 2)
        head = delete_node(head, 4)
        self.assertEqual([5], [x for x in head])
        head = reverse(head)
        self.assertEqual([5], [x for x in head])

if __name__ == '__main__':
    unittest.main()

