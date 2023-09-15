import sympy as sym

x = sym.Symbol("x")
yes = 0
for a in range(0, 20):
    a /= 2
    # if sym.simplify(a*(x+3)) == sym.simplify(5*x+15-x):
    #     print(sym.simplify(a*(x+3)), "!=", sym.simplify(5*x+15-x), "            a =", a, "YES")
    #     yes += 1
    # else:
    #     print(sym.simplify(a*(x+3)), "!=", sym.simplify(5*x+15-x), "            a =", a, "NO")
    print(sym.simplify(a*(x+3)), " > ", sym.simplify(5*x+15-x), "    =", sym.reduce_inequalities(sym.simplify(a*(x+3)) > sym.simplify(5*x+15-x)), a)

print(yes)