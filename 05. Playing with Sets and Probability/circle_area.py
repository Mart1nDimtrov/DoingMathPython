'''
#5: Estimating the Area of a Circle
Estimate the area of a circle by throwing darts at 
a dartboard with a circle of radius r inscribed in a square with side 2r.
As the number of throws grow estimate the value of pi.
'''
import math
import random

def calculate_area(radius, points):
	center = (radius, radius)

	in_circle = 0
	for i in range(points):
		x = random.uniform(0, 2*radius)
		y = random.uniform(0, 2*radius)
		p = (x, y)
		# distance of the point created from circle's center
		d = math.sqrt((p[0]-center[0])**2 + (p[1]-center[1])**2)
		if d <= radius:
			in_circle += 1
	area_of_square = (2*radius)**2
	return (in_circle/points)*area_of_square

radius = float(input('Radius: '))
area_of_circle = math.pi*radius**2
for points in [10**3, 10**5, 10**6]:
    print('Area: {0}, Estimated ({1} darts): {2}'.format(area_of_circle, points, calculate_area(radius, points)))
    print('The estimation of pi is {0}'.format(calculate_area(radius, points)/4))