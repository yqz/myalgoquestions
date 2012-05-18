#!/usr/bin/python

"""
QUESTION: Give an array of ids, find the minimum non-negative id that is not in the array.
Example: [3,1,0,2,5], the min value should 4 that is not in the list.
"""

def partition(a, l, h, x):
    """ Partition function that will make elements that are less than x
    on one side of the array. And the other side will be greater or equal
    to x. return the index of first element on the right side"""
    i = j = l 
    # [l, j) contains elemnts less than x.
    # [j, i) contains elements greater or equal to x
    for i in range(l, h):
        if a[i] <= x:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
            j += 1
    return j


def _lowest_free_id(a, s, n):
    if n == 0:
        print s
        return s
    mid = s + n/2
    p = partition(a, s, s + n, mid)
    if p - s  < mid - s + 1:
        return _lowest_free_id(a, s, p - s)
    elif p - s  == mid - s + 1:
        return _lowest_free_id(a, p, s+n-p)
    else:
        assert False


def lowest_free_id(a):
    return _lowest_free_id(a, 0, len(a))



import unittest

class MyUnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_func(self):
        a = [0,1,2,3,4,5,6,7]
        self.assertEqual(partition(a, 0, 8, 4), 5)
        self.assertEqual(0, 
                len([x for x in a[0:5] if x > 4]))
        self.assertEqual(0, 
                len([x for x in a[5:] if x <= 4]))
        a.sort()
        self.assertEqual([0,1,2,3,4,5,6,7], a)
                
        a = [1,0,3,2,4,6,7,5]
        self.assertEqual(partition(a, 0, 8, 4), 5)
        self.assertEqual(0, 
                len([x for x in a[0:5] if x > 4]))
        self.assertEqual(0, 
                len([x for x in a[5:] if x <= 4]))
        a.sort()
        self.assertEqual([0,1,2,3,4,5,6,7], a)

    def test_func2(self):
        #import random
        #a = [0,2,3,4,5,6,7,8]
        #self.assertEqual(1, lowest_free_id(a))
        #for i in range(10):
        #    random.shuffle(a)
        #    self.assertEqual(1, lowest_free_id(a))

        #a = [1,2,3]
        #self.assertEqual(0, lowest_free_id(a))
        #for i in range( 0):
        #    random.shuffle(a)
        #    self.assertEqual(0, lowest_free_id(a))

        #a = [3,5,6,7,1,2]
        #self.assertEqual(0, lowest_free_id(a))
        a = [3,0,5,6,7,1,2]
        self.assertEqual(4, lowest_free_id(a))
        #a = [3,0,5,6,7,1,2,4]
        #self.assertEqual(8, lowest_free_id(a))
        #a = [0,2]
        #self.assertEqual(1, lowest_free_id(a))
        #a = [100,12,2,3,0,1,7,6,]
        #self.assertEqual(4, lowest_free_id(a))
        #a = [100,99,98,97]
        #self.assertEqual(0, lowest_free_id(a))

if __name__ == '__main__':
    unittest.main()

