'''
#3: Experiment with Other CSV difference
You can experiment with numerous interesting difference sources freely available 
on the Internet. The website http://www.quandl.com/is one such source. For 
this challenge, download the following difference as a CVS file from http://www
.quandl.com/WORLDBANK/USA_SP_POP_TOTL/: the total population 
of the United States at the end of each year for the years 1960 to 2012. 
Then, calculate the mean, median, variance, and standard deviation of 
the differencein population over the years and create a graph showing these 
differences.
'''
import csv 
import matplotlib.pyplot as plt 
from collections import Counter

def plot_difference(x, y):
	plt.plot(x, y)
	plt.xlabel('Years')
	plt.ylabel('Difference')
	plt.title('Population difference for the last 55 years')
	plt.show()

def read_csv(filename):
	numbers = []
	with open(filename) as f:
		reader = csv.reader(f)
		next(reader)
		for row in reader:
			numbers.append(float(row[1]))
		return list(reversed(numbers))

def calc_difference(population):
	difference = []
	for index in range(1, len(population)):
		difference.append(abs(population[index] - population[index - 1]))
	return difference

def calculate_mean(numbers):
	s = sum(numbers)
	N = len(numbers)
	mean = s/N

	return mean

def calculate_mode(numbers):
	c = Counter(numbers)
	mode = c.most_common(1)
	return mode[0][0]

def calculate_median(numbers):
	N = len(numbers)
	numbers.sort()

	# Find the median
	if N % 2 == 0:
		# if N is even
		m1 = N/2
		m2 = (N/2) + 1
		# Convert to integer, match position
		m1 = int(m1) - 1
		m2 = int(m2) - 1
		median = (numbers[m1] + numbers[m2])/2
	else:
		m =(N+1)/2
		# Convert to integer, match position
		m = int(m) - 1
		median = numbers[m]

	return median

def find_differences(numbers):
	# Find the mean
	mean = calculate_mean(numbers)
	# Find the differences from the mean
	diff = []
	for num in numbers:
		diff.append(num - mean)

	return diff

def calculate_variance(numbers):
	# Find the list of differences
	diff = find_differences(numbers)
	# Find the squared differences
	squared_diff = []
	for d in diff:
		squared_diff.append(d**2)
	sum_squared_diff = sum(squared_diff)
	variance = sum_squared_diff / len(numbers)
	return variance

population = read_csv('WORLDBANK-USA_SP_POP_TOTL.csv')
difference = calc_difference(population)
years = [x for x in range(1961, 2015)] # we exclude the first year since we only count the difference
print(difference)
mean = calculate_mean(difference)
median = calculate_median(difference)
mode = calculate_mode(difference)
variance = calculate_variance(difference)
standard_deviation = variance**0.5

print('Mean: {0}'.format(mean))
print("Median: {0}".format(median))
print("Mode: {0}".format(mode))
print("Variance: {0}".format(variance))
print("Standard deviation: {0}".format(standard_deviation))
plot_difference(years, difference)
