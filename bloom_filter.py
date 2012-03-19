#!/usr/bin/python

class BloomFilter(object):
    """A typical Bloom Filter.
    The bloom filter will use 2**(buckets_exp) buckets.
    func will be an array of hash functions.
    """
    def __init__(self, buckets_exp, *funcs):
        self._total_buckets = 1 << buckets_exp
        self._buckets = bytearray(self._total_buckets >> 3) if buckets_exp > 3 \
                        else bytearray(1)
        self._hash_funcs = funcs
        self._mod = (1 << buckets_exp) - 1

    def _set_bit(self, x):
        """Set the xth bit"""
        assert x >= 0 and x < self._total_buckets
        self._buckets[x >> 3] |= (1 << (x & 7))

    def _is_set(self, x):
        """Test if xth bit is set"""
        assert x >= 0 and x < self._total_buckets
        return self._buckets[x >> 3] & (1 << (x & 7))

    def add(self, obj):
        """Add an object into store."""
        for func in self._hash_funcs:
            self._set_bit(func(obj) & self._mod)

    def contains(self, obj):
        """Test if an object is already in store.
        This function should have 0 false negative rate,
        but >0 false positive rate.
        """
        for func in self._hash_funcs:
            if not self._is_set(func(obj) & self._mod):
                return False
        return True

    def union(self, bf):
        """Union the current bloom filter with another
        bloom filter (bf)"""
        assert self._total_buckets == bf._total_buckets
        for i in range(len(self._buckets)):
            self._buckets[i] |= bf._buckets[i]
        

import unittest

class MyUnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_func(self):
        f = BloomFilter(6, hash)
        f.add('abc')
        f.add('bcd')

        self.assertEqual(True, f.contains('abc'))
        self.assertEqual(True, f.contains('bcd'))
        self.assertEqual(False, f.contains('cd'))

        g = BloomFilter(6, hash)
        g.add('egf')
        g.add('wxy')
        self.assertEqual(True, g.contains('egf'))
        self.assertEqual(True, g.contains('wxy'))
        self.assertEqual(False, g.contains('abc'))

        g.union(f)
        self.assertEqual(True, g.contains('abc'))
        self.assertEqual(True, g.contains('wxy'))
        self.assertEqual(False, g.contains('cd'))




        

if __name__ == '__main__':
    unittest.main()
