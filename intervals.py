#!/usr/bin/python
# -*- coding: utf-8 -*-
import tree

"""
QUESTION:
    一个range的序列（链表或数组），如[1,3], [2,6], [8,10]，[15,18]
    写程序合并有重叠的range，比如上面的序列合并为[1,6], [8,10], [15,18]
    如果这个序列不是静态的，而是一个数据流，如何 处理？"""

def are_intervals_intersecting(i1, i2):
    """return if two intervals have overlap"""
    return not (i1[0] > i2[1] or i1[1] < i2[0])

def interval_union(i1, i2):
    """union two overlapping interval"""
    assert are_intervals_intersecting(i1, i2)
    return (min(i1[0], i2[0]), max(i1[1], i2[1]))

class IntervalLL(object):
    """Use Linked List to solve the problem"""
    class _Node(object):
        def __init__(self, interval):
            self.interval = interval
            self.next = None

    def __init__(self):
        self.head = None

    def add(self, interval):
        """Add a interval to link list. O(N)"""
        if self.head is None:
            self.head = self._Node(interval)
        else:
            prev = None
            cur = self.head
            # Find the first interval that is not on the left of the
            # inserting interval
            while cur is not None and cur.interval[1] < interval[0]:
                prev = cur
                cur = cur.next
            if cur is None:
                # if there is node on the right of the interval,
                # just append it to the tail of the linkedlist.
                prev.next = self._Node(interval)
            else:
                newnode = self._Node(interval)
                # Allocate a new interval which will intersects
                # with all following intervals and add it to LL.
                while cur is not None and are_intervals_intersecting(cur.interval, newnode.interval):
                    newnode.interval = interval_union(newnode.interval, cur.interval)
                    cur = cur.next
                newnode.next = cur
                if prev is None:
                    self.head = newnode
                else:
                    prev.next = newnode

    def intervals(self):
        node = self.head
        while node is not None:
            yield node.interval
            node = node.next

class IntervalTree(object):
    """Interval tree. All intervals inside the tree shall
    not overlap each other"""
    class _Node(object):
        def __init__(self, interval):
            self.interval = interval
            self.left = None
            self.right = None
        def left_cut(self, masternode, x):
            if x < self.interval[0]:
                if self.left is not None:
                    self.left = self.left.left_cut(masternode, x)
                return self
            if x >= self.interval[0] and x <= self.interval[1]:
                masternode.interval = interval_union(masternode.interval, self.interval)
                return self.right
            if x > self.interval[1]:
                if self.right is not None:
                    return self.right.left_cut(masternode, x) 
                else:
                    return None
        def right_cut(self, masternode, x):
            if x > self.interval[1]:
                if self.right is not None:
                    self.right = self.right.right_cut(masternode, x)
                return self
            if x <= self.interval[1] and x >= self.interval[0]:
                masternode.interval = interval_union(masternode.interval, self.interval)
                return self.left
            if x < self.interval[0]:
                if self.left is not None:
                    return self.left.right_cut(masternode, x) 
                else:
                    return None
                    



    def __init__(self):
        self.root = None

    def add(self, interval):
        """Adding a interval to the tree."""
        if self.root is None:
            self.root = self._Node(interval)
        else:
            # Find the first that overlaps.
            node = self.root
            while True:
                if interval[1] < node.interval[0]:
                    if node.left is not None:
                        node = node.left
                    else:
                        # Add a new leaf node since there's no
                        # overlap
                        node.left = self._Node(interval)
                        break
                elif interval[0] > node.interval[1]:
                    if node.right is not None:
                        node = node.right
                    else:
                        # Add a new leaf node since there's no
                        # overlap
                        node.right = self._Node(interval)
                        break
                else:
                    # Overlap found, we need to extend the current 
                    # node to the union of the node the do a left/right
                    # cut.
                    oe = node.interval[1]
                    os = node.interval[0]
                    node.interval = interval_union(node.interval, interval)
                    if interval[1] > oe and node.right is not None:
                        node.right = node.right.left_cut(node, interval[1])
                    if interval[0] < os and node.left is not None:
                        node.left = node.left.right_cut(node, interval[0])
                    break
    def intervals(self):
        r = []
        def addtor(node):
            r.append(node.interval)
        tree.inorder_traversal_iterative_2(self.root, addtor)
        return r






import unittest

class MyUnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_func(self):
        il = IntervalLL()
        il.add((1,3))
        il.add((2,6))
        il.add((8,10))
        il.add((15,18))
        self.assertEqual(list(il.intervals()), [(1, 6), (8, 10), (15, 18)])
        il.add((9,14))
        self.assertEqual(list(il.intervals()), [(1, 6), (8, 14), (15, 18)])
        il.add((13,17))
        self.assertEqual(list(il.intervals()), [(1, 6), (8, 18)])
        il.add((-1, 1))
        self.assertEqual(list(il.intervals()), [(-1, 6), (8, 18)])
        il.add((-4, -3))
        self.assertEqual(list(il.intervals()), [(-4,-3),(-1, 6), (8, 18)])
        il.add((20, 23))
        self.assertEqual(list(il.intervals()), [(-4,-3),(-1, 6), (8, 18), (20, 23)])
        il.add((-100, 100))
        self.assertEqual(list(il.intervals()), [(-100, 100)])

    def test_func2(self):
        il = IntervalTree()
        il.add((1,3))
        il.add((2,6))
        il.add((8,10))
        il.add((15,18))
        self.assertEqual(list(il.intervals()), [(1, 6), (8, 10), (15, 18)])
        il.add((9,14))
        self.assertEqual(list(il.intervals()), [(1, 6), (8, 14), (15, 18)])
        il.add((13,17))
        self.assertEqual(list(il.intervals()), [(1, 6), (8, 18)])
        il.add((-1, 1))
        self.assertEqual(list(il.intervals()), [(-1, 6), (8, 18)])
        il.add((-4, -3))
        self.assertEqual(list(il.intervals()), [(-4,-3),(-1, 6), (8, 18)])
        il.add((20, 23))
        self.assertEqual(list(il.intervals()), [(-4,-3),(-1, 6), (8, 18), (20, 23)])
        il.add((-100, 100))
        self.assertEqual(list(il.intervals()), [(-100, 100)])
if __name__ == '__main__':
    unittest.main()

