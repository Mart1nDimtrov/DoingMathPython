'''
#1: Verify the Continuity of a Function at a Point
Your challenge here is to write a program that will (1) accept a single variable function and a value of that variable as inputs and (2) check 
whether the input function is continuous at the point where the variable 
assumes the value input.
'''

from sympy import Derivative, Limit, Symbol, S, sympify, solve

def check_continuity(f, var, point):
	f = sympify(f)
	lp = Limit(f, var, point, dir='+').doit()
	ln = Limit(f, var, point, dir='-').doit()
	if lp == ln:
		print("{0} is continuous at {1}".format(f, point))
	else:
		print("{0} is discontinuous at {1}".format(f, point))



f = input('Enter a function in one variable: ')
var = input('Enter the variable to differentiate with respect to: ')
point = float(input('Enter the point to check continuity at: '))

check_continuity(f, var, point)


