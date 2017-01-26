'''
#1: Factor Finder 
You learned about the factor()function, which prints the factors of an 
expression. Now that you know how your program can handle expressions 
input by a user, write a program that will ask the user to input an expression, calculate its factors, and print them. Your program should be able to 
handle invalid input by making use of exception handling.
'''
from sympy import Symbol, expand, factor
from sympy.core.sympify import SympifyError


x = Symbol('x')
y = Symbol('y')
expr = input('Enter your expression in terms of x and y: ')
try:
	expr = expand(expr)
except SympifyError:
	print('Invalid input')
else:
	print(factor(expr))