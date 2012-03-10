#!/usr/bin/python

"""
QUESTION:
    Given a set A of integers (NO duplicate), find out the maximum range [a,b] that 
    all number between a,b are in the set A.
"""

def max_range(A):
    """ There is an O(n) approach that use a hashmap to store the maximum
    range starting/ending at any point. Let's say m[x] is the maximum range
    starting/ending at m[x]. So for any new integer x, we just look at its 
    neighbors, and update neighbors accordingly"""
    m = {}
    max_length = 0
    for x in A:
        left = m[x-1] if (x -1) in m else 0
        right = m[x+1] if (x+1) in m else 0
        length = left + right + 1
        m[x - left] = length
        m[x + right] = length
        if length > max_length:
            max_length = length
    return max_length

import unittest

class MyUnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_func(self):
        self.assertEqual(max_range([1,3,5,4,2,6]), 6)  
        self.assertEqual(max_range([1,3,5,6,2]), 3)  
        self.assertEqual(max_range([1,3,5,2,6,8,9,7]), 5)  

if __name__ == '__main__':
    unittest.main()


