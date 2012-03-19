#!/usr/bin/python

"""
QUESTION: Classical KMP string matching implementation.
"""

def kmp_preprocess(p):
    b = [-1]
    i = 0
    j = -1
    while i < len(p):
        while j >= 0 and p[i] != p[j]:
            j = b[j]
        i += 1
        j += 1
        b.append(j)
    return b

def kmp_match(doc, p):
    """ Find the 1st occurence of p in doc"""
    i = 0
    j = 0
    b = kmp_preprocess(p)
    while i < len(doc):
        while j >= 0 and doc[i] != p[j]:
            j = b[j]
        i += 1
        j += 1
        if j == len(p):
            return i - j
    return -1


import unittest

class MyUnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_func(self):
        doc = "abcdabcdeabdedacdbde"
        pattern = "abded"
        self.assertEqual(doc.find(pattern), kmp_match(doc, pattern))
        doc = "abcdabcdeabdedacdbde"
        pattern = "abdcdabc"
        self.assertEqual(doc.find(pattern), kmp_match(doc, pattern))
        doc = "abcdabcdeabdedacdbde"
        pattern = "abdedac"
        self.assertEqual(doc.find(pattern), kmp_match(doc, pattern))
        doc = "abcdabcdeabdedacdbde"
        pattern = "abdx"
        self.assertEqual(doc.find(pattern), kmp_match(doc, pattern))

if __name__ == '__main__':
    unittest.main()

