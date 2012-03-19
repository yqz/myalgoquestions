#!/usr/bin/python

"""
QUESTION: Push all the zero's of a given array to the end of the array. 
In place only. Ex 1,2,0,4,0,0,8 becomes 1,2,4,8,0,0,0
"""

def arrange_0(a):
    j = i = len(a) - 1
    for i in range(len(a) -1, -1, -1):
        if a[i] == 0:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
            j -= 1
    return a


import unittest

class MyUnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_func(self):
        self.assertEqual([2,1,3,0,0], arrange_0([2,0,3,1,0]))
        self.assertEqual([2,1,3,0,0], arrange_0([2,1,3,0,0]))
        self.assertEqual([2,3,1,0,0], arrange_0([0,0,1,2,3]))
        self.assertEqual([], arrange_0([]))
        self.assertEqual([1], arrange_0([1]))
        self.assertEqual([0], arrange_0([0]))
        self.assertEqual([1,0], arrange_0([0,1]))

if __name__ == '__main__':
    unittest.main()

