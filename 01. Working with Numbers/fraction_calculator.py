'''
4: Fraction Calculator
Write a calculator that can perform the basic mathematical operations on 
two fractions. It should ask the user for two fractions and the operation the 
user wants to carry out.
'''

from fractions import Fraction

def add(a, b):
    print("Result of Addition: {0}".format(a + b))
    
def subtract(a, b):
    print("Result of Subtraction: {0}".format(a - b))
    
def multiply(a, b):
    print("Result of Multiplication: {0}".format(a * b))

def divide(a, b):
    print("Result of Division: {0}".format(a / b))

    
a = input('Enter first fraction: ')
a = Fraction(a)
b = input('Enter second fraction: ')
b = Fraction(b)

op = input("Operation to perform - Add, Subtract, Divide, Multiply: ").lower()

if op == "add":
    add(a,b)
elif op == "subtract":
    subtract(a,b)
elif op == "multiply":
    multiply(a,b)
elif op == "divide":
    divide(a,b)
    
