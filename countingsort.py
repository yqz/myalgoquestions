#!/usr/bin/python

def sort(a, minval, maxval):
    c = [0]*(maxval - minval + 1)
    offset = minval
    # First iteration: Compute histogram
    for x in a:
        c[x - offset] += 1

    # second iteration: Compute the number
    # of elements tha tis smaller than i in
    # array c
    total = 0
    for i in range(0, maxval - minval + 1):
        t = c[i]
        c[i] = total
        total += t

    # 3rd iteration: put the element into
    # correct position
    output = [None]*len(a)
    for x in a:
        output[c[x-offset]] = x
        c[x-offset] += 1
    return output

import unittest

class MyUnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_func(self):
        a = [3,14, 2, -1, 1, 3, 4, 6 ,5 , 2, 3, 7 , 0, -2]
        a = sort(a, -2, 14)
        self.assertEqual(a, sorted(a))
        a = [3,14, 2, -1, 1, 2, 2, -2,  3, 4, 6 ,5 , 2, 3, 7 , 0, -2]
        a = sort(a, -100, 100)
        self.assertEqual(a, sorted(a))

if __name__ == '__main__':
    unittest.main()       
    
