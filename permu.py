#!/usr/bin/python

def _permu(A, i, func):
    if i == len(A) - 1:
        func(A)
        return
    for j in range(i, len(A)):
        temp = A[i]
        A[i] = A[j]
        A[j] = temp
        _permu(A, i + 1,func)
        temp = A[i]
        A[i] = A[j]
        A[j] = temp

def permu(A,func):
    if len(A) == 1:
        func(A)
        return
    _permu(A,0, func)


import unittest

class MyUnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_func(self):
        L = []
        def  func(A):
            L.append(tuple(A[:]))
        permu([1,2,3,4], func)
        L.sort()
        import itertools
        base = [x for x in itertools.permutations([1,2,3,4])]
        self.assertEqual(L, base)

if __name__ == '__main__':
    unittest.main()
