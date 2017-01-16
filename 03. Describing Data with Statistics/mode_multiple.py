'''
Calculating the mode when the list of numbers may
have multiple modes
'''

from collections import Counter

def calculate_mode(numbers):
	c = Counter(numbers)
	numbers_freq = c.most_common()
	max_count = numbers_freq[0][1]

	modes = []
	for num in numbers_freq:
		if num[1] == max_count:
			modes.append(num[0])
	return modes


scores = [5, 5, 5, 4, 4, 4, 9, 1, 3]
modes = calculate_mode(scores)
print('The mode(s) of the list are:')
for mode in modes:
	print(mode)