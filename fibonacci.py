#! usr/bin/env python
# Fibonacci.py - A quick introduction to using generators **WOW**

from random import randint as r_Int

def fib():
    a,b = 0,1
    while 1:
        yield a
        a,b = b, a + b

** BEGIN CODE **
try:
    g = fib()
    for it in range(15):
        next(g)

except Exception as e:
    raise Exception('Exception Occurred when {}'.format(e))

