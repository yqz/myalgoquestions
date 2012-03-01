#!/usr/bin/python

"""
QUESTION:
|_|
|_| |_|
|_| |_| |_|
|_| |_| |_| |_|
|_| |_| |_| |_| |_|

Each cup has capacity C and once a cup gets full, it drops half extra amount to left child and half extra amount to right child

for Eg : let' first cups get 2C amount of liquid then extra amount C(2C-C) will be divided equally to left and right child cup of next level

i.e. C/2 to left child and C/2 to right child

Write a function which takes input parameter as amount of liquid poured at top (L) and height of cup (h) and capacity (C) and it should print amount of liquid absorbed in all cup.
"""

def solve(L, h, C):
    # allocate cups.
    cups = [float(L)]
    for i in range(1, h):
        print [c > C and C or c for c in cups]
        cups_next = [0]*(i+1)
        for j in range(len(cups_next)):
            cups_next[j] += (cups[j] - C)/2 if j < len(cups) and cups[j] > C else 0
            cups_next[j] += (cups[j-1] - C)/2 if j -1 >= 0 and cups[j-1] > C else 0
        cups = cups_next
    # print the last level
    print [c > C and C or c for c in cups]


import unittest

class MyUnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_func(self):
        solve(40, 4, 5)

if __name__ == '__main__':
    unittest.main()


