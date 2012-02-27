#!/usr/bin/python

def binary_search(a, x):
    """search element x in sorted array a,
    return the index of the element.
    None if not found"""
    l = 0
    h = len(a) - 1
    while l <= h:
        mid = (l + h)/2
        if a[mid] == x:
            return mid
        elif x < a[mid]:
            h = mid - 1
        else:
            l = mid + 1

def lower_bound(a, x):
    """Search the max element in 'a' that
    is less or equal than x. return the 
    index of the element. If x is less than
    min(a), return None"""
    l = 0
    h = len(a) - 1
    result = None
    while l <= h:
        mid = (l+h)/2
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            h = mid - 1
        else:
            result = mid
            l = mid + 1
    return result

def strict_lower_bound(a, x):
    """Search the max element in 'a' that
    is less than x. return the 
    index of the element. If x is less than
    min(a), return None"""
    l = 0
    h = len(a) - 1
    result = None
    while l <= h:
        mid = (l+h)/2
        if x <= a[mid]:
            h = mid - 1
        else:
            result = mid
            l = mid + 1
    return result

import unittest

class MyUnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_func(self):
        a = [2,4,6,8,10,12]
        for i, x in enumerate(a):
            self.assertEqual(i, binary_search(a, x))
        self.assertEqual(None, binary_search(a, 0))
        self.assertEqual(None, binary_search(a, 100))

    def test_func2(self):
        a = [2,4,6,8,10,12]
        for i, x in enumerate(a):
            self.assertEqual(i, lower_bound(a, x))
        self.assertEqual(0, lower_bound(a, 3))
        self.assertEqual(1, lower_bound(a, 5))
        self.assertEqual(None, lower_bound(a, 0))
        self.assertEqual(len(a)-1, lower_bound(a, 100))

    def test_func3(self):
        a = [2,4,6,8,10,12]
        for i, x in enumerate(a):
            self.assertEqual(None if i == 0 else i - 1, strict_lower_bound(a, x))
        self.assertEqual(0, strict_lower_bound(a, 3))
        self.assertEqual(1, strict_lower_bound(a, 5))
        self.assertEqual(None, strict_lower_bound(a, 0))
        self.assertEqual(None, strict_lower_bound(a, 2))
        self.assertEqual(len(a)-1, strict_lower_bound(a, 100))

if __name__ == '__main__':
    unittest.main()
