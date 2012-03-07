#!/usr/bin/python

"""
QUESTION: given a set of intervals, return two intervals that have the largest overlap.
Assume the intervals are sorted already.
"""

def overlap(i1, i2):
    return min(i1[1], i2[1]) - max(i1[0], i2[0]) 

def max_interval_overlap(a):
    """a is the sorted interval list. 
    O(n) time"""
    r1 = r2 = None
    max_overlap = 0
    if len(a) < 2:
        return r1, r2
    i,j = 0,1
    while j < len(a):
        if a[j][0] < a[i][1]:
            ov = overlap(a[i], a[j])
            if ov > max_overlap:
                max_overlap,r1,r2 = ov,i,j
            if a[j][1] >= a[i][1]:
                i = j
        else:
            i = j
        j += 1
    return (r1, r2) if max_overlap > 0 else (None, None)

import unittest

class MyUnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_func(self):
        a = [(1,5), (2,3), (3,4),(3, 8), (4,9)]
        self.assertEqual((3,4), max_interval_overlap(a))
        a = [(1,6), (2,3), (3,4),(3, 8)]
        self.assertEqual((0,3), max_interval_overlap(a))
        a = [(1,6), (2,4), (3,4)]
        self.assertEqual((0,1), max_interval_overlap(a))
        a = [(1,2), (2,3), (3,4)]
        self.assertEqual((None,None), max_interval_overlap(a))

if __name__ == '__main__':
    unittest.main()
