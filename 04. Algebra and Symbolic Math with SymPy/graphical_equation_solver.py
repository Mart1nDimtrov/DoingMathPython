'''
#2: Graphical Equation Solver
Earlier, you learned how to write a program that prompts the user to input 
an expression such as 3x+ 2y− 6 and create the corresponding graph. Write 
a program that asks the user for two expressions and then graphs them both, 
as follows:
>>> expr1 = input('Enter your first expression in terms of x and y: ')
>>> expr2 = input('Enter your second expression in terms of x and y: ')
Now, expr1and expr2will store the two expressions input by the user. 
You should convert both of these into SymPy objects using the sympify()step 
in a try...except block.
All you need to do from here is plot these two expressions instead 
of one.
Once you’ve completed this, enhance your program to print the 
solution—the pair of x and y values that satisfies both equations. This 
will also be the spot where the two lines on the graph intersect. (Hint: 
Refer to how we used the solve()function earlier to find the solution of a 
system of two linear equations.)
'''

from sympy import Symbol, sympify, solve
from sympy.plotting import plot
from sympy.core.sympify import SympifyError


def plot_expression(expr1, expr2):
	x = Symbol('x')
	print(solve((expr1, expr2), dict=True))
	p = plot(expr1, expr2, legend=True, show=False)
	p[0].line_color = 'b'
	p[1].line_color = 'r'
	p.show()


expr1 = input('Enter the first expression in terms of x: ')
expr2 = input('Enter the second expression in terms of x: ')
try:
	expr1 = sympify(expr1)
	expr2 = sympify(expr2)
except SympifyError:
	print('Invalid input')
else:
	plot_expression(expr1, expr2)

	
