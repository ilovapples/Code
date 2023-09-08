from sympy import *
import random

largest_int = 0
formula_for_largest_int = 0

for i in range(29000):
    x = Symbol('x')
    s = []
    while len(s) < 6:
        for k in range(6):
            l = random.randint(1,9)
            if l not in s:
                s.append(l)
            elif l in s:
                continue
    j = Eq((s[0]/s[1])*x+s[2],(s[3]/s[4])*x+s[5])
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
        if special_p > largest_int and int(special_p) == special_p:
            largest_int = int(special_p)
            formula_for_largest_int = s
        print("0"*(7-(len(str(i+1)))) + str(i+1) + ": " + str(special_p), end='')
    print("      Formula: ({}/{})*x + {} = ({}/{})*x + {}".format(s[0],s[1],s[2],s[3],s[4],s[5]))
print("Biggest number = " + str(largest_int))
print("Formula for biggest number: ({}/{})*x + {} = ({}/{})*x + {}".format(formula_for_largest_int[0],formula_for_largest_int[1],formula_for_largest_int[2],formula_for_largest_int[3],formula_for_largest_int[4],formula_for_largest_int[5]))
