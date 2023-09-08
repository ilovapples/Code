from sympy import *
import random

clst2zero = 9000
formula_for_clst2zero = []

for i in range(70000):
    x = Symbol('x')
    s = []
    while len(s) < 4:
        for k in range(4):
            l = random.randint(1,9)
            if l not in s:
                s.append(l)
            elif l in s:
                continue
    j = Eq(s[0]*x + s[1],s[2]*x + s[3])
    p = solve([j], (x))
    try:
        p.keys()
        p_type = "dict"
        special_p=p[list(p.keys())[0]]
    except AttributeError:
        p_type = "list"
    if p_type == 'list':
        print("0"*(7-(len(str(i+1)))) + str(i+1) + ": No Real Solution (Invalid)",end='')
    else:
        if abs(special_p) < clst2zero:
            clst2zero = special_p
            formula_for_clst2zero = s
        print("0"*(7-(len(str(i+1)))) + str(i+1) + ": " + str(special_p), end='')
    print("      Formula: {}*x + {} = {}*x + {}".format(s[0],s[1],s[2],s[3]))

print("Closest number to zero = " + str(clst2zero))
print("Formula for closest number to zero: {}*x + {} = {}*x + {}".format(formula_for_clst2zero[0],formula_for_clst2zero[1],formula_for_clst2zero[2],formula_for_clst2zero[3]))
