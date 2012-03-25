#!/usr/bin/python

"""
QUESTION: rotate a matrix clockwise for 90 degree in place.
"""
import math

def rotate_90(a):
    n = len(a)
    # So this is a n*n matrix with m rows n columns.
    for i in range(int(math.ceil(float(n)/2))):
        for j in range(int(math.floor(float(n)/2))):
            temp = a[i][j]
            a[i][j] = a[n-1-j][i]
            a[n-1-j][i] = a[n-1-i][n-1-j]
            a[n-1-i][n-1-j] = a[j][n-1-i]
            a[j][n-1-i] = temp

import unittest

class MyUnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_func(self):
        a = [[1]]
        rotate_90(a)
        self.assertEqual([[1]], a)
        a = [[1,2],[3,4]]
        rotate_90(a)
        self.assertEqual([[3,1],[4,2]], a)
        a = [[1,2,3],[4,5,6],[7,8,9]]
        rotate_90(a)
        self.assertEqual([[7,4,1],[8,5,2],[9,6,3]], a)

if __name__ == '__main__':
    unittest.main()



