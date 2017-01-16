'''
#1: Better Correlation Coefficient–Finding Program
The find_corr_x_y()function we wrote earlier to find the correlation 
coefficient between two sets of numbers assumes 
that the two sets of numbers are the same length. 
Improve the function so that it first checks the 
length of the lists. If they’re equal, only then should the function proceed 
with the remaining calculations; otherwise, it should print an error message 
that the correlation can’t be found.
'''
import matplotlib.pyplot as plt 

def find_corr_x_y(x, y):
	n = len(x)

	# Find the sum of the products
	prod = []
	for xi,yi in zip(x,y):
		prod.append(xi*yi)

	sum_prod_x_y = sum(prod)
	sum_x = sum(x)
	sum_y = sum(y)
	squared_sum_x = sum_x**2
	squared_sum_y = sum_y**2

	x_square = []
	for xi in x:
		x_square.append(xi**2)
	# Find the sum_x
	x_square_sum = sum(x_square)

	y_square=[]
	for yi in y:
		y_square.append(yi**2)
	# Find the sum 
	y_square_sum = sum(y_square)

	# Use the formula to calculate correlation 
	numerator = n*sum_prod_x_y - sum_x*sum_y
	denominator_term1 = n*x_square_sum - squared_sum_x
	denominator_term2 = n*y_square_sum - squared_sum_y
	denominator = (denominator_term1*denominator_term2)**0.5
	correlation = numerator / denominator

	return correlation

grades = [83, 85, 84, 96, 94, 86, 87, 97, 97, 85]
test_scores = [85, 87, 86, 97, 96, 88, 89, 98, 98, 87]
if len(grades) == len(test_scores):
	print("The correlations is: " + str(find_corr_x_y(grades, test_scores)))
	plt.scatter(grades, test_scores)
	plt.show()
else:
	print("Error! Correlation cannot be found.")
