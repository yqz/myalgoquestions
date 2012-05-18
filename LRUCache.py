#!/usr/bin/python

class _Node(object):
    """A doubly circular linked list"""
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = None

    def detach(self):
        self.prev.next = self.next
        self.next.prev = self.prev

    def insert_after(self, node):
        node.next = self.next
        node.prev = self
        self.next.prev = node
        self.next = node

    def insert_before(self, node):
        node.prev = self.prev
        node.next = self
        self.prev = node

    def __str__(self):
        return str(self.key) + ':' + str(self.value)

    #def __repr__(self):
    #    return str(self.key) + ':' + str(self.value)

class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self._cache = {}
        # Dummy head for the linked list
        self._head = _Node(None, None)
        self._head.next = self._head
        self._head.prev = self._head


    def add(self, key, value):
        if key in self._cache:
            node = self._cahce[key]
            node.detach()
            node = _Node(key, value)
            self._head.insert_after(node)
            self._cache[key] = node 
        else:
            node = _Node(key, value)
            self._head.insert_after(node)
            self._cache[key] = node

        while len(self._cache) > self.capacity:
            node = self._head.prev
            node.detach()
            del self._cache[node.key]


    def get(self, key):
        if key in self._cache:
            node = self._cache[key]
            node.detach()
            self._head.insert_after(node)
            return node.value
        else:
            return None

import unittest

class MyUnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_func(self):
        cache = LRUCache(3)
        self.assertEqual(None, cache.get('a'))
        cache.add('a',1)
        self.assertEqual(1, cache.get('a'))
        cache.add('b', 2)
        cache.add('c', 3)
        self.assertEqual(3, cache.get('c'))
        self.assertEqual(1, cache.get('a'))
        # b should be swapped out
        cache.add('d', 4)
        self.assertEqual(None, cache.get('b'))
        self.assertEqual(1, cache.get('a'))
        # c should be swapped out
        cache.add('e', 5)
        self.assertEqual(None, cache.get('c'))
        self.assertEqual(5, cache.get('e'))

if __name__ == '__main__':
    unittest.main()

