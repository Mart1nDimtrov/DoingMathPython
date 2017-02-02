'''
#3: Exploring Hénon’s Function
Your challenge here is to write a program to create a graph showing 
20,000 iterations of this transformation, starting with the point (1, 1).
'''
import matplotlib.pyplot as plt

def transform(x, y):
	x2, y2 = x, y
	x2 = y + 1 - (1.4*(x**2))
	y2 = 0.3 * x
	return x2, y2

def plot_function():
	x = 1
	y = 1
	x_coord = []
	y_coord = []
	for i in range(20000):
		x, y = transform(x, y)
		x_coord.append(x)
		y_coord.append(y)
	plt.scatter(x_coord, y_coord)
	plt.show()

plot_function()



