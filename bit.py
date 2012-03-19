#!/usr/bin/python

"""
A simple implmentation of Binary Index Tree.
"""
class BinaryIndexTree(object):
    def __init__(self, n):
        """Accept a integer or a list.
        if it's integer, it will be taken as the 
        size of the binary index tree.
        if it's list, it will be taken as the initial
        array, and we will compute tree value from it
        """
        if isinstance(n, list):
            self.tree = [0]*(len(n)+1)
            for idx, data in enumerate(n):
                self.incr(idx, data)
        else:
            self.tree = [0]*(n+1)

    def incr(self, idx, val):
        """Increase the value at idx by val."""
        idx += 1
        while idx  < len(self.tree):
            self.tree[idx] += val
            idx += (idx & (-idx))

    def sum(self, idx):
        """return cumulative sum from 0 to idx"""
        idx += 1
        r = 0
        while idx > 0:
            r += self.tree[idx]
            idx -= (idx & (-idx))
        return r



import unittest

class MyUnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_func(self):
        t = BinaryIndexTree(8)
        self.assertEqual(0, t.sum(1))
        t.incr(0, 10)
        self.assertEqual(10, t.sum(1))
        self.assertEqual(10, t.sum(7))
        self.assertEqual(10, t.sum(0))
        t.incr(7, 20)
        self.assertEqual(10, t.sum(1))
        self.assertEqual(30, t.sum(7))
        t.incr(3, 15)
        self.assertEqual(10, t.sum(0))
        self.assertEqual(10, t.sum(1))
        self.assertEqual(10, t.sum(2))
        self.assertEqual(25, t.sum(3))
        self.assertEqual(25, t.sum(4))
        self.assertEqual(25, t.sum(5))
        self.assertEqual(25, t.sum(6))
        self.assertEqual(45, t.sum(7))

    def test_func2(self):
        t = BinaryIndexTree([1,2,3,4,5,6,7,8])
        self.assertEqual(1, t.sum(0))
        self.assertEqual(3, t.sum(1))
        self.assertEqual(6, t.sum(2))
        self.assertEqual(10, t.sum(3))
        self.assertEqual(36, t.sum(7))


if __name__ == '__main__':
    unittest.main()



        
