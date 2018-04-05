#! usr/bin/env python
#github.py - A test to see how to Github on Atom

import os, re
# Fibonacci.py - A quick introduction to using generators **WOW**
from random import randint as r_Int

def fib():
    a,b = 0,1
    while 1:
        yield a
        a,b = b, a + b

try:
    g = fib()
    for it in range(15):
        next(g)

except Exception as e:
    raise Exception('Exception Occurred when {}'.format(e))
