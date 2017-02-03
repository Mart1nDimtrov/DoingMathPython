from sympy import Limit, Symbol, S

x = Symbol('x')
l = Limit(1/x, x, S.Infinity)
print(l.doit())
