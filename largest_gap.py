#!/usr/bin/python

"""
QUESTION: In an array A, find max(j - i) where i < j and a[i] < a[j]
"""

def naive_gap(a):
    """ This is the n square naive approach"""
    m = 0
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] < a[j] and j - i > m:
                m = j - i
    return m


def gap(a):
    """ This is an O(n) approach, we keep another array
    b which b[i] = max(a[j]) where j >= i. Then for a[i]
    we can easily find the largest gap starting from i."""
    n = len(a)
    if n == 1: 
        return 0
    b = [0]*n
    b[n - 1] = a[n - 1]
    for i in range(n - 2, -1, -1):
        b[i] = max(b[i+1], a[i])
    i = 0
    j = 0
    m = 0
    while i < n and j < n:
        while j < n and a[i] < b[j]:
            if j - i > m:
                m = j - i
            j += 1
        i += 1
    return m
        

import unittest

class MyUnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_func(self):
        a = [1,2,3,4,5,6]
        self.assertEqual(5, naive_gap(a))
        a = [1]
        self.assertEqual(0, naive_gap(a))
        a = [1,2]
        self.assertEqual(1, naive_gap(a))
        a = [2,1]
        self.assertEqual(0, naive_gap(a))
        a = [9,8,7,6,5,4,3,2,1]
        self.assertEqual(0, naive_gap(a))
        a = [4,2,7,6,5,4,3,2,1]
        self.assertEqual(5, naive_gap(a))

    def test_func2(self):
        a = [1,2,3,4,5,6]
        self.assertEqual(5, gap(a))
        a = [1]
        self.assertEqual(0, gap(a))
        a = [1,2]
        self.assertEqual(1, gap(a))
        a = [2,1]
        self.assertEqual(0, gap(a))
        a = [9,8,7,6,5,4,3,2,1]
        self.assertEqual(0, gap(a))
        a = [4,2,7,6,5,4,3,2,1]
        self.assertEqual(5, gap(a))

    def test_func3(self):
        import random
        n = 100
        r = 1000
        for i in range(0, r):
            a = []
            for j in range(0, n):
                a.append(random.randint(0, n))
            self.assertEqual(naive_gap(a), gap(a))


if __name__ == '__main__':
    unittest.main()

