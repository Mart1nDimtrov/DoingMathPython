from sympy import Symbol, Limit, S
n = Symbol('n', positive=True)
p = Symbol('p', positive=True)
r = Symbol('r', positive=True)
t = Symbol('t', positive=True)
print(Limit(p*(1+r/n)**(n*t), n, S.Infinity).doit())
