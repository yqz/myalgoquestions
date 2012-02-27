#!/usr/bin/python

def parent(i):
    return (i - 1)/2

def lch(i):
    return i*2 + 1

def rch(i):
    return i*2 + 2

class BinaryHeap(object):
    def __init__(self):
        self.heap = []

    def insert(self, x):
        self.heap.append(x)
        BinaryHeap._bubble_up(self.heap, len(self.heap) - 1)

    def extract_max(self):
        return self.heap[0] if len(self.heap) > 0 else None

    def pop_max(self):
        if len(self.heap) > 0:
            r = self.heap[0]
            if len(self.heap) > 1:
                self.heap[0] = self.heap.pop()
                BinaryHeap._bubble_down(self.heap, 0)
            else:
                self.heap.pop()
            return r
        else:
            return None

    @staticmethod
    def _bubble_down(a, i):
        """perform a bubble down operation"""
        while True:
            l = lch(i)
            r = rch(i)
            maxi = -1
            if l < len(a):
                maxi = l
                maxv = a[l]
            else:
                break
            if r < len(a) and a[r] > maxv:
                maxv = a[r]
                maxi = r

            if a[i] < maxv:
                a[maxi] = a[i]
                a[i] = maxv
                i = maxi
            else:
                break

    @staticmethod
    def _bubble_up(a, i):
        """perform a bubble up operation"""
        while i > 0:
            p = parent(i)
            if a[i] > a[p]:
                t = a[i]
                a[i] = a[p]
                a[p] = t
                i = p
            else:
                break

import unittest

class MyUnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_func(self):
        h = BinaryHeap()
        x = [3,1,2,3,5,6,8,6,2,10,9,-1,-3]
        for i in x:
            h.insert(i)

        y = []
        p = h.pop_max()
        while p is not None:
            y.append(p)
            p = h.pop_max()

        self.assertEqual(y, sorted(x, reverse=True))



if __name__ == '__main__':
    unittest.main()
