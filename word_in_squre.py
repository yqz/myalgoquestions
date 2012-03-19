#!/usr/bin/python

"""
QUESITON: There's a 4x4 square. Each square contains a character.
You are also given a dictionary. Find if all words in the dictionary
that can be formed by characters in the square. The word from the square
is formed by starting at any given point and travel two neighboring 8
directions. Characters can't be reused.

Example:
    A B S H 
    E O Y E
    I R P L
    M G O L 

Dictionary:
    BOY,BORG,HELL,HELP

All words in the dictionary should be able to be found in the square.
"""
import trie

N = 4

# All 8 directions offset table
directions = [(x,y) for x in range(-1, 2) for y in range(-1,2) if not (x == 0 and y == 0)]

def isvalid_pos(pos):
    return pos[0] >= 0 and pos[0] < N and pos[1] >= 0 and pos[1] < N

def dfs_solve(square, current_pos, current_word, visited, dictionary):
    if dictionary.has_word(current_word):
        print '*' + current_word
    for d in directions:
        new_pos = (current_pos[0] + d[0], current_pos[1] + d[1])
        if isvalid_pos(new_pos) and not new_pos in visited:
            new_word = current_word + square[new_pos[0]][new_pos[1]]
            if dictionary.has_prefix(new_word):
                visited.add(new_pos)
                dfs_solve(square, new_pos, new_word, visited, dictionary)
                visited.remove(new_pos)


def solve(square, words):
    # First build a trie from words
    dictionary = trie.Trie()
    for word in words:
        dictionary.add(word)

    # A visited set, so that we won't travel to the 
    # same cel twice.
    visited = set()
    for i in range(0, N):
        for j in range(0, N):
            visited.clear()
            visited.add((i,j))
            dfs_solve(square, (i,j), square[i][j], visited, dictionary)

import unittest

class MyUnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_func(self):
        square = [['A', 'B', 'S', 'H' ], ['E', 'O', 'Y', 'E'], \
                ['I', 'R', 'P', 'L'], ['M', 'G', 'O', 'L']]
        words = ["RIP", "BOYSB", "DET", "KATH", "BOY", "BOYS", "BORG", "HELL", "HELP"]
        solve(square, words)

if __name__ == '__main__':
    unittest.main()
