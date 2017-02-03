'''
Derivative calculator 
'''
from sympy import Symbol, Derivative, sympify, pprint
from sympy.core.sympify import SympifyError
def derivative(f, var):
	var = Symbol(var)
	d = Derivative(f, var).doit()
	pprint(d)

f = input('Enter a function: ')
var = input('Enter the variable to differentiate with respect to: ')
try:
	f = sympify(f)
except SympifyError:
	print('Invalid input')
else:
	derivative(f, var)