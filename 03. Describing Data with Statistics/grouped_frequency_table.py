'''
#5: Creating a Grouped Frequency Table
For this challenge, your task is to write a program that creates a grouped 
frequency table from a set of numbers. A grouped frequency table displays 
the frequency of data classified into different classes. For example, let’s consider the scores we discussed in “Creating a Frequency Table” on page 69: 
7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, and 10. A grouped frequency 
table would display this data as follows:
Grade Frequency
1–6 	6
6 –11 	14
The table classifies the grades into two classes: 1–6 (which includes 
1 but not 6) and 6–11 (which includes 6 but not 11). It displays against 
them the number of grades that belong to each category. Determining 
the number of classes and the range of numbers in each class are two key 
steps involved in creating this table. In this example, I’ve demonstrated two 
classes with the range of numbers in each class equally divided between 
the two.
Here’s one simple approach to creating classes, which assumes the 
number of classes can be arbitrarily chosen:

def create_classes(numbers, n):
	low = min(numbers) 
	high = max(numbers)
	# Width of each class
	width = (high - low)/n
	classes = []
	a = low
	b = low + width
	classes = []
	while a < (high-width):
		classes.append((a, b))
		a = b 
		b = a + width 
	# The last class may be of a size that is less than width 
	classes.append((a, high+1))
	return classes
The create_classes()	function accepts two arguments: a list of numbers, 
numbers, and n, the number of classes to create. It’ll return a list of tuples 
with each tuple representing a class. For example, if it’s called with numbers 
7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10, and n= 4, it returns the 
following list: [(1, 3.25), (3.25, 5.5), (5.5, 7.75), (7.75, 11)]. Once you have 
the list, the next step is to go over each of the numbers and find out which 
of the returned classes it belongs to.
Your challenge is to write a program to read a list of numbers from 
a file and then to print the grouped frequency table, making use of the 
create_classes()function.
'''

def create_classes(numbers, n):
	low = min(numbers) 
	high = max(numbers)
	# Width of each class
	width = (high - low)/n
	classes = []
	a = low
	b = low + width
	classes = []
	while a < (high-width):
		classes.append((a, b))
		a = b 
		b = a + width 
	# The last class may be of a size that is less than width 
	classes.append((a, high+1))
	return classes

def print_table(numbers, classes):
	print("Grade 		Frequency")
	for couple in classes:
		frequency = 0
		for number in numbers:
			if number >= couple[0] and number < couple[1]:
				frequency+=1
		print("{0}-{1} 		{2}".format(int(couple[0]), int(couple[1]), frequency))


numbers = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
classes = create_classes(numbers, 4)
print_table(numbers, classes)



