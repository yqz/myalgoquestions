#!/usr/bin/python

def f():
    x = 10
    def g():
        print x
    g()
    print x
    x = 20
    g()
    print f.func_dict 
    print g.__closure__

f()
