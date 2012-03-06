#!/usr/bin/python

"""
QUESTION: given two sorted array A, B, find 1 element from each array that 
SUMs to K
"""

def find(a, b, k):
    i = 0
    j = len(b) - 1
    while i < len(a) and j >= 0:
        if a[i] + b[j] > k:
            j -= 1
        elif a[i] + b[j] < k:
            i += 1
        else:
            return i,j
    return None

import unittest

class MyUnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_func(self):
        a = [1,5,7,9,12,100]
        b = [5,8,7,10,11,67]
        self.assertEqual((1,0),find(a,b, 10))
        self.assertEqual(None,find(a,b, 100))
        self.assertEqual((3,4),find(a,b, 20))
        self.assertEqual(None,find(a,b, 33))

if __name__ == '__main__':
    unittest.main()
