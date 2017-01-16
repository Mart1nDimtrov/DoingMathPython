'''
#2: Exploring a Quadratic Function Visually
In Chapter 1, you learned how to find the roots of a quadratic equation, 
such as x
2
+ 2x+ 1 = 0. We can turn this equation into a function by writing 
it as y= x
2
+ 2x+ 1. For any value of x, the quadratic function produces some
value for y. For example, when x= 1, y= 4. Here’s a program that calculates 
the value of yfor six different values of x:
''
Quadratic function calculator
''
# Assume values of x
ux_values = [-1, 1, 2, 3, 4, 5] 
for x in x_values:
# Calculate the value of the quadratic function
y = x**2 + 2*x + 1
print('x={0} y={1}'.format(x, y))
At u, we create a list with six different values for x. The forloop starting at vcalculates the value of the function above for each of these values 
and uses the label yto refer to the list of results. Next, we print the value of 
xand the corresponding value of y. When you run the program, you should 
see the following output:
x=-1 y=0
x=1 y=4
x=2 y=9
x=3 y=16
x=4 y=25
x=5 y=36
Notice that the first line of the output is a root of the quadratic equation because it’s a value for xthat makes the function equal to 0.
Your programming challenge is to enhance this program to create 
a graph of the function. Try using at least 10 values for xinstead of the 6 
above. Calculate the corresponding yvalues using the function and then 
create a graph using these two sets of values.
Once you’ve created the graph, spend some time analyzing how the 
value of yvaries with respect to x. Is the variation linear or nonlinear?
'''
import matplotlib.pyplot as plt
# Assume values of x
x_values = [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
y_values = []
for x in x_values:
# Calculate the value of the quadratic function
	y = x**2 + 2*x + 1
	y_values.append(y)

plt.plot(x_values, y_values)
plt.title("Range of the quadratic function")
plt.xlabel('values of x')
plt.ylabel('values of y', labelpad=20) # move the label from the baseline
plt.axis((0, 10, 0, 100))
plt.yticks(range(0, 100, 5))
plt.show()




