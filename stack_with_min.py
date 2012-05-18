#!/usr/bin/python

class StackWithMin(object):
    def __init__(self):
        self._data = []
        self._min = []

    def push(self, x):
        m = self.min()
        self._min.append(min(m, x) if m is not None else x)
        self._data.append(x)

    def pop(self):
        self._min.pop()
        return self._data.pop()

    def min(self):
        return self._min[-1] if len(self._min) > 0 else None

    def __len__(self):
        return len(self._data)
                
