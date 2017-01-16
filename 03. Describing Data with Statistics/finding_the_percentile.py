'''
#4: Finding the Percentile
The percentile is a commonly used statistic that conveys the value below 
which a given percentage of observations falls. For example, if a student 
obtained a 95 percentile score on an exam, this means that 95 percent of 
the students scored less than or equal to the student’s score. For another 
example, in the list of numbers 5, 1, 9, 3, 14, 9, and 7, the 50th percentile 
is 7 and the 25th percentile is 3.5, a number that is not present in the list. 
There are a number of ways to find the observation corresponding to a 
given percentile, but here’s one approach.
Let’s say we want to calculate the observation at percentile p:
1.  In ascending order, sort the given list of numbers, which we might 
call data.
2.  Calculate 
i = (n * p / 100) + 0.5
where n is the number of items in data.
3.  If i is an integer, data[i]is the number corresponding to percentile p.
4.  If i is notan integer, set k equal to the integral part of i and f equal to 
the fractional part of i. The number (1-f)*data[k] + f*data[k+1] is the 
number at percentile p.
Using this approach, write a program that will take a set of numbers in 
a file and display the number that corresponds to a specific percentile supplied as an input to the program.
''' 
import math

def calc_percentile(numbers, percentile):
	numbers = sorted(numbers)
	print(numbers)
	length = len(numbers)
	i = ((length * percentile) / 100) + 0.5
	if i.is_integer():
		return numbers[int(i) - 1] # take into account the correct position
	else:
		fraction, whole = math.modf(i) 
		w = int(whole)
		# also take into account the correct position in the array
		number = ((1 - fraction) * numbers[w - 1]) + (fraction*numbers[(w + 1) - 1])
		return number
		

numbers = [5, 1, 9, 3, 14, 9, 7]
print(calc_percentile(numbers, 25))




