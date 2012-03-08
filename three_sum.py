#!/usr/bin/python

"""
QUESTION: given array A of integers, find three integers in the array
that has sum to K.
"""

def three_sum(A, K):
    if len(A) < 3:
        return None
    # sort the array.
    A.sort()
    for i in range(0, len(A) - 2):
        if A[i]*3 > K:
            return None
        j = i + 1
        k = len(A) - 1
        while j < k:
            if A[i] + A[j] + A[k] == K:
                return A[i],A[j],A[k]
            elif A[i] + A[j] + A[k] < K:
                j += 1
            else:
                k -= 1
    return None

import unittest

class MyUnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_func(self):
        A = [3,8,5,2,1,4,5]
        self.assertEqual(None, three_sum(A,100))
        self.assertEqual((1,2,8), three_sum(A,11))
        self.assertEqual((1,4,8), three_sum(A,13))
        self.assertEqual((5,5,8), three_sum(A,18))
        self.assertEqual(None, three_sum(A,19))

if __name__ == '__main__':
    unittest.main()


