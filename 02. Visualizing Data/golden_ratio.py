'''
#5: Exploring the Relationship Between the Fibonacci Sequence and the 
Golden Ratio
The Fibonacci sequence (1, 1, 2, 3, 5, . . .) is the series of numbers where 
the ith number in the series is the sum of the two previous numbers—that 
is, the numbers in the positions (i− 2) and (i− 1). The successive numbers in this series display an interesting relationship. As you increase the 
number of terms in the series, the ratios of consecutive pairs of numbers 
are nearly equal to each other. This value approaches a special number 
referred to as the golden ratio. Numerically, the golden ratio is the number 
1.618033988 . . . , and it’s been the subject of extensive study in music, architecture, and nature. For this challenge, write a program that will plot on a 
graph the ratio between consecutive Fibonacci numbers for, say, 100 numbers, which will demonstrate that the values approach the golden ratio.
You may find the following function, which returns a list of the first n
Fibonacci numbers, useful in implementing your solution:
def fibo(n): 
	if n == 1: 
		return [1]
	if n == 2:
		return [1, 1]
	# n > 2
	a = 1
	b = 1
	# First two members of the series
	series = [a, b]
	for i in range(n):
		c = a + b
		series.append(c) 
		a = b
		b = c
	return series 

The output of your solution should be a graph, as shown in Figure 2-18.
'''

import numpy as np
import matplotlib.pyplot as plt

def fibo(n): 
	if n == 1: 
		return [1]
	if n == 2:
		return [1, 1]
	# n > 2
	a = 1
	b = 1
	# First two members of the series
	series = [a, b]
	for i in range(n):
		c = a + b
		series.append(c) 
		a = b
		b = c
	return series

series = fibo(100)
#print(len(series))
x_values = np.array([x for i, x in enumerate(series) if i % 2 == 0])
y_values = np.array([x for i, x in enumerate(series) if i % 2 == 1])

#print(y_values)
ratios = np.array([y / x for x, y in zip(x_values, y_values)]) # y values are bigger
numbers =  np.array([float(x) for x in range(0, 51)])
plt.plot(numbers, ratios)
plt.title("Ratio between consecutive Fibonacci numbers")
plt.xlabel("No.")
plt.ylabel("Ratio")
plt.show()
