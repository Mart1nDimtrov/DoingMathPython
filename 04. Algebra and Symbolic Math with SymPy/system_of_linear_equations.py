from sympy import Symbol, solve, pprint

x = Symbol('x')
y = Symbol('y')
expr1 = 2*x + 3*y - 6
expr2 = 3*x + 2*y - 12

# call the solve function with the two expressions forming a tuple
print(solve((expr1, expr2), dict=True))

# find if the solution really satisfies the equations
soln = solve((expr1, expr2), dict=True)
soln = soln[0]
print(expr1.subs({x:soln[x], y:soln[y]}))
print(expr2.subs({x:soln[x], y:soln[y]}))