#!/usr/bin/python

import pdb


def sort(a, l=None, r=None):
    l = l or 0
    r = r or len(a) 

    flag = True
    iteration = 0
    while flag:
        flag = False
        for i in range(l, r - iteration - 1):
            if a[i] > a[i+1]:
                # Swap
                t = a[i]
                a[i] = a[i+1]
                a[i+1] = t
                flag = True
        iteration += 1


import unittest

class MyUnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_func(self):
        a = [3,14, 2, -1, 1, 3, 4, 6 ,5 , 2, 3, 7 , 0, -2]
        sort(a)
        self.assertEqual(a, sorted(a))
        a = [1, 3, 2]
        sort(a, 1, 3)
        self.assertEqual(a, sorted(a))

if __name__ == '__main__':
    unittest.main()
