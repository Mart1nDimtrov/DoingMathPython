'''
#4: Solving Single-Variable Inequalities
You’ve seen how to solve an equation using SymPy’s solve()function. But 
SymPy is also capable of solving single-variable inequalities, such as x + 5 > 3 
and sinx − 0.6 > 0. That is, SymPy can solve relations besides equality, like 
>, <, and so on. For this challenge, create a function, isolve(), that will take 
any inequality, solve it, and then return the solution. 
First, let’s learn about the SymPy functions that will help you implement this. The inequality-solving functions are available as three separate 
functions for polynomial, rational, and all other inequalities. We’ll need to 
pick the right function to solve various inequalities, or we’ll get an error.
'''

from sympy import Poly, Symbol, solve, sympify, solve_poly_inequality, solve_rational_inequalities, solve_univariate_inequality, sin
from sympy.core.sympify import SympifyError

x = Symbol('x')
expr = input("Please enter the expression you want to solve: ")
expr = sympify(expr)
if (expr.is_polynomial()):
	lhs = expr.lhs
	p = Poly(lhs, x)
	rel = ineq_obj.rel_op
	print(solve_poly_inequality(p, rel))
elif(expr.is_rational_function()):
	lhs = expr.lhs
	numer, denom = lhs.as_numer_denom()
	p1 = Poly(numer)
	p2 = Poly(denom)
	rel = ineq_obj.rel_op
	print(solve_rational_inequalities([[((p1, p2), rel)]]))
else:
	try:
		ineq_obj = expr
	except SympifyError:
		print("Invalid input")
	else:
		print(solve_univariate_inequality(ineq_obj, x, relational=False))
	
	



