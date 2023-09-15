from sympy import *

x = Symbol("x")
for a in range(100):
    j = Eq(8*x-8+3*a*x, 5*a*x-2*a)
    print(solve([j], (x)), "a =", a)