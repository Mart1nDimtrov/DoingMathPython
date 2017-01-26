from sympy import Symbol, solve

x = Symbol('x')
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')

expr = a*x*x + b*x + c
print(solve(expr, x, dict=True))

