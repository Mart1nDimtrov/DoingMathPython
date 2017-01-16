'''
#2: Statistics Calculator 
Implement a statistics calculator that takes a list of numbers in the file 
mydata.txt and then calculates and prints their mean, median, mode, 
variance, and standard deviation using the functions we wrote earlier in 
this chapter.
'''
from collections import Counter

def read_data(filename):

	numbers = []
	with open(filename) as f:
		for line in f:
			numbers.append(float(line))

	return numbers

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

data = read_data('mydata.txt')
mean = calculate_mean(data)
median = calculate_median(data)
mode = calculate_mode(data)
variance = calculate_variance(data)
standard_deviation = variance**0.5

print('Mean: {0}'.format(mean))
print("Median: {0}".format(median))
print("Mode: {0}".format(mode))
print("Variance: {0}".format(variance))
print("Standard deviation: {0}".format(standard_deviation))