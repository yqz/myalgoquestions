#!/usr/bin/python

"""
QUESTION: We have an array of size n. The array
should support the following operations efficiently.

1. Range Add: I want to add a value to elements i..j 
    in array.
2. Query: I want to Query the number for element i.

Using BIT, we should get O(logn) for both operation.

Suppose the original array is A. We construct a new array
B where A[i] = B[0] + B[1] + ... + B[i] so B[i] = A[i] - A[i-1].
For operation 1, when we add a value to A[i..j], what we
need to do is to add value to B[i] so that A[i..j] all 
get the value increase because A[i] is cumulative function
of array B. In order to not add val to value outside of range,
we need to decrease B[j + 1] by val too.

So, for array B, the two operations become:
    1. Add a value to two array elements.
    2. Query SUM(B[0..i])

The above two operations can easily achieve O(nlogn) using
binary index tree.

Pratical usage of this array A:
1. Suppose we have a stream of integers, at any given point
we want to query how many elements are smaller than k? Or
we can query for the kth smallest value so far. 

2. Given a stream of intervals, we want to query, how many 
intervals covers point x so far?
"""

import bit

class FastRangeAddArray(object):
    def __init__(self, n):
        self._b = bit.BinaryIndexTree(n)
        self.n = n

    def add(self, i, j, val):
        self._b.incr(i, val)
        if j + 1 < self.n: 
            self._b.incr(j + 1, -val)

    def query(self, i):
        return self._b.sum(i)

    def array(self):
        return [self.query(i) for i in range(self.n)]

import unittest

class MyUnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_func(self):
        a = FastRangeAddArray(8)
        self.assertEqual([0,0,0,0,0,0,0,0], a.array())
        a.add(0, 7, 1)
        self.assertEqual([1,1,1,1,1,1,1,1], a.array())
        a.add(0, 8, -1)
        self.assertEqual([0,0,0,0,0,0,0,0], a.array())
        a.add(0, 8, 0)
        self.assertEqual([0,0,0,0,0,0,0,0], a.array())
        a.add(0, 3, 2)
        self.assertEqual([2,2,2,2,0,0,0,0], a.array())
        a.add(2, 5, 1)
        self.assertEqual([2,2,3,3,1,1,0,0], a.array())


if __name__ == '__main__':
    unittest.main()


