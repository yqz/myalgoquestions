#!/usr/bin/python

"""
QUESTION: find the min value from a sorted rotated array.
Example: 3,5,6,1,2 RETURN 1
"""

def shift_array(a, n):
    return a[n:] + a[:n]

def rotated_sorted_min(a):
    i = 0
    j = len(a) - 1
    while i <= j:
        if i == j:
            return a[i]
        elif j - i == 1:
            return min(a[i], a[j])
        mid = (i + j)/2
        if a[i] < a[mid]:
            if a[mid] < a[j]:
                j = mid -1
            else:
                i = mid + 1
        else:
            j = mid

import unittest

class MyUnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_func(self):
        a = [1,2,3,4,5,6,7,8,9,10]
        for i in range(len(a)):
            self.assertEqual(1, rotated_sorted_min(shift_array(a,i)))
        a = [1,2,3,4,5,6,7,8,9]
        for i in range(len(a)):
            self.assertEqual(1, rotated_sorted_min(shift_array(a,i)))

if __name__ == '__main__':
    unittest.main()


