'''
#4: Visualizing Your Expenses
I always find myself asking at the end of the month, “Where did all that 
money go?” I’m sure this isn’t a problem I alone face. 
For this challenge, you’ll write a program that creates a bar chart for 
easy comparison of weekly expenditures. The program should first ask for 
the number of categories for the expenditures and the weekly total expenditure in each category, and then it should create the bar chart showing 
these expenditures. 
Here’s a sample run of how the program should work:
Enter the number of categories: 4
Enter category: Food
Expenditure: 70
Enter category: Transportation
Expenditure: 35
Enter category: Entertainment
Expenditure: 30
Enter category: Phone/Internet
Expenditure: 30

A bar chart can be created using matplotlib’s barh()function, which 
is also defined in the pyplotmodule. Figure 2-17 shows a bar chart that 
illustrates the number of steps I walked during the past week. The days of 
the week—Sunday, Monday, Tuesday, and so forth—are referred to as the 
labels. Each horizontal bar starts from the y-axis, and we have to specify the 
y-coordinate of the centerof this position for each of the bars. The length of 
each bar corresponds to the number of steps specified. 
he following program creates the bar chart:
''
Example of drawing a horizontal bar chart
''
import matplotlib.pyplot as plt
def create_bar_chart(data, labels):
# Number of bars
num_bars = len(data)
# This list is the point on the y-axis where each
# Bar is centered. Here it will be [1, 2, 3...]
upositions = range(1, num_bars+1)
vplt.barh(positions, data, align='center')
# Set the label of each bar
plt.yticks(positions, labels)
plt.xlabel('Steps')
plt.ylabel('Day')
plt.title('Number of steps walked')
# Turns on the grid which may assist in visual estimation
plt.grid( 
plt.show()
if __name__ == '__main__':
# Number of steps I walked during the past week
steps = [6534, 7000, 8900, 10786, 3467, 11045, 5095]
# Corresponding days
labels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
create_bar_chart(steps, labels)
The create_bar_chart()function accepts two parameters—data, which 
is a list of numbers we want to represent using the bars and labels, and the 
corresponding labelslist. The center of each bar has to be specified, and 
I’ve arbitrarily chosen the centers as 1, 2, 3, 4, and so on using the help of 
the range()function at u. 
We then call the barh()function, passing positionsand dataas the first 
two arguments and then the keyword argument, align='center', at v. The 
keyword argument specifies that the bars are centered at the positions on 
the y-axis specified by the list. We then set the labels for each bar, the axis 
labels, and the title using the yticks()function. We also call the grid()function to turn on the grid, which may be useful for a visual estimation of the 
number of steps. Finally, we call the show()function.
'''

import matplotlib.pyplot as plt

def create_bar_chart(data, labels):
	# Number of bars
	num_bars = len(data)
	# This list is the point on the y-axis where each
	# Bar is centered. Here it will be [1, 2, 3...]
	positions = range(1, num_bars+1)
	plt.barh(positions, data, align='center')
	# Set the label of each bar
	plt.yticks(positions, labels)
	plt.xlabel('Amount')
	plt.ylabel('Categories')
	plt.title('Weekly expenditures')
	# Turns on the grid which may assist in visual estimation
	plt.grid()
	plt.show()


categories_count = int(input("Enter the number of categories: "))
expenditures = []
categories = []

while (categories_count > 0):
	try:
		category = input('Enter category: ')
		expenditure = float(input('Expenditure: '))
		categories.append(category)
		expenditures.append(expenditure)
	except ValueError:
		print('You entered an invalid input')
	else:
		categories_count = categories_count - 1
			

create_bar_chart(expenditures, categories)

