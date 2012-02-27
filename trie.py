#!/usr/bin/python

class Trie(object):
    class _TrieNode(object):
        def __init__(self):
            self.is_end = False

    def __init__(self):
        self.root = self._TrieNode()
    
    def add(self, word):
        node = self.root
        for ch in word:
            if hasattr(node, ch):
                node = getattr(node, ch)
            else:
                newNode = self._TrieNode()
                setattr(node, ch, newNode)
                node = newNode
        node.is_end = True

    def has_word(self, word):
        node = self.root
        for ch in word:
            if not hasattr(node, ch):
                return False
            node = getattr(node, ch)
        return node.is_end 

    def has_prefix(self, word):
        node = self.root
        for ch in word:
            if not hasattr(node, ch):
                return False
            node = getattr(node, ch)
        return True

import unittest

class MyUnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_func(self):
        t = Trie()
        t.add('abc')
        t.add('bce')
        t.add('abcdef')
        self.assertEqual(t.has_word('abc'), True)
        self.assertEqual(t.has_word('bce'), True)
        self.assertEqual(t.has_word('xe'), False)
        self.assertEqual(t.has_word('a'), False)
        self.assertEqual(t.has_word('abcd'), False)
        self.assertEqual(t.has_word('abcdef'), True)
        self.assertEqual(t.has_word('abcdefgh'), False)

        self.assertEqual(t.has_prefix('abc'), True)
        self.assertEqual(t.has_prefix('bce'), True)
        self.assertEqual(t.has_prefix('xe'), False)
        self.assertEqual(t.has_prefix('a'),  True)
        self.assertEqual(t.has_prefix('abcd'), True)
        self.assertEqual(t.has_prefix('abcdef'), True)
        self.assertEqual(t.has_prefix('abcdefgh'), False)
        self.assertEqual(t.has_prefix('acd'), False)

        self.assertEqual(t.root.a.b.c.is_end, True)
        self.assertEqual(t.root.a.b.c.d.is_end, False)
        self.assertEqual(t.root.b.c.e.is_end, True)

if __name__ == '__main__':
    unittest.main()


