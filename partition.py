#!/usr/bin/python

"""
QUESTION: Quick sort partition function
"""

def partition(a, p):
    """
    Parition array a by pivot a[p].
    """
    if a is None or len(a) == 1:
        return 0
    # Swap a[p] to the last position
    pivot = a[p]
    a[p] = a[len(a) - 1]
    a[len(a) - 1] = pivot

    j = 0
    k = 0
    # [0..j-1] contains elements that is smaller than pivot.
    # [j..k-1] contains elements that is greater or equal to pivot.
    # [0..k-1] is all the elements that is processed so far.
    while k < len(a) - 1:
        if a[k] >= pivot:
            k += 1
        else:
            t = a[k]
            a[k] = a[j]
            a[j] = t
            j += 1
            k += 1
    # swap pivot to a[j]
    a[len(a) - 1] = a[j]
    a[j] = pivot
    return j, a


import unittest

class MyUnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_func(self):
        print partition([5,5,5,5,5,5], 2)

if __name__ == '__main__':
    unittest.main()







