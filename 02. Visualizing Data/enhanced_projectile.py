'''
#3: Enhanced Projectile Trajectory Comparison Program
Your challenge here is to enhance the trajectory comparison program in 
a few ways. First, your program should print the time of flight, maximum 
horizontal distance, and maximum vertical distance traveled for each of the 
velocity and angle of projection combinations.
The other enhancement is to make the program work with any number 
of initial velocity and angle of projection values, supplied by the user. For 
example, here’s how the program should ask the user for the inputs:
How many trajectories? 3
Enter the initial velocity for trajectory 1 (m/s): 45
Enter the angle of projection for trajectory 1 (degrees): 45
Enter the initial velocity for trajectory 2 (m/s): 60
Enter the angle of projection for trajectory 2 (degrees): 45
Enter the initial velocity for trajectory(m/s) 3: 45
Enter the angle of projection for trajectory(degrees) 3: 90
Your program should also ensure that erroneous input is properly 
handled using a try...excep block, just as in the original program.
'''

import matplotlib.pyplot as plt
import math

def frange(start, final, increment):
	numbers = []
	while start < final:
		numbers.append(start)
		start = start + increment
	return numbers

def draw_trajectory(u, theta):

	theta = math.radians(theta)
	g = 9.8

	# Time of flight
	t_flight = 2*u*math.sin(theta)/g
	# Find time intervals
	intervals = frange(0, t_flight, 0.001)
	# List of x and y coordinates
	x = []
	y = []
	for t in intervals:
		x.append(u*math.cos(theta)*t)
		y.append(u*math.sin(theta)*t - 0.5*g*t*t)

	draw_graph(x, y)

def draw_graph(x, y):
	plt.plot(x, y)
	plt.xlabel('x-coordinate')
	plt.ylabel('y-coordinate')
	plt.title('Projectile motion of a ball')
	


times = int(input("How many trajectories?\n"))
legends = times

while (times > 0):
	try:
		u = float(input('Enter the initial velocity (m/s): '))
		theta = float(input('Enter the angle of projection (degrees): '))
	except ValueError:
		print('You entered an invalid input')
	else:
		times = times - 1
		draw_trajectory(u, theta)

plt.legend(["velocity"+ str(x)  for x in range(0, legends + 1)])	
plt.show()



