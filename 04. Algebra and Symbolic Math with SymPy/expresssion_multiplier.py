'''
Product of two expressions
'''

from sympy import expand, sympify
from sympy.core.sympify import SympifyError

def product(expr1, expr2):
	prod = expand(expr1*expr2)
	print(prod)

expr1 = input("Enter the first expression: ")
expr2 = input("Enter the second expression: ")

try:
	expr1 = simpify(expr1)
	expr2 = simpify(expr2)
except SympifyError:
	print("Invalid input")
else:
	product(expr1, expr2)