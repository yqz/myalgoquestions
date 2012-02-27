#! /usr/bin/python

import bubblesort

def partition(a, l, r):
    pivot = a[r - 1]
    p = l
    i = l
    while i < r - 1:
        if a[i] >= pivot:
            i += 1
        else:
            t = a[p]
            a[p] = a[i]
            a[i] = t
            p += 1
            i += 1
    t = a[p]
    a[r - 1] = a[p]
    a[p] = pivot
    return p


def sort(a, l=None, r=None):
    l = l or 0
    r = r or len(a)
    if r - l > 1:
        if r - l < 5:
            # if there are less than 5 elements
            # use bubble sort
            bubblesort.sort(a, l, r)
        else:
            p = partition(a, l, r)
            sort(a, l, p)
            sort(a, p + 1, r)


import unittest

class MyUnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_func(self):
        a = [3,14, 2, -1, 1, 3, 4, 6 ,5 , 2, 3, 7 , 0, -2]
        sort(a)
        self.assertEqual(a, sorted(a))

if __name__ == '__main__':
    unittest.main()
