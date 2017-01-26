from sympy import Symbol
from sympy.plotting import plot

x = Symbol('x')
p = plot((2*x+3), (x, -5, 5), title='A Line', xlabel='x', ylabel='2x+3')
p.save('line.png')
