'''
Plot the graph of an input expression
'''

from sympy import Symbol, sympify, solve
from sympy.plotting import plot
from sympy.core.sympify import SympifyError

def plot_expression(expr):
	y = Symbol('y')
	solutions = solve(expr, y)
	expr_y = solutions[0]
	plot(expr_y)


expr = input('Enter your expression in terms of x and y: ')
try:
	expr = sympify(expr)
except SympifyError:
	print('Invalid input')
else:
	plot_expression(expr)
