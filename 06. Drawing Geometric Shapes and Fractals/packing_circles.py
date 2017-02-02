'''
#1: Packing Circles into a Square
I mentioned earlier that matplotlib supports the creation of other geometric shapes. The Polygonpatch is especially interesting, as it allows you to 
draw polygons with different numbers of sides.
In this challenge, you’ll attempt a very simplified version of the “circles 
packed into a square” problem. How many circles of radius 0.5 will fit in the 
square produced by this code? Draw and find out! Figure 6-11 shows how 
the final image will look.
'''
from matplotlib import pyplot as plt

def draw_circle(x, y):
	circle = plt.Circle((x, y), radius = 0.5) 
	return circle
	

def draw_square():
	ax = plt.axes(xlim = (0, 6), ylim = (0, 6))
	square = plt.Polygon([(1, 1), (5, 1), (5, 5), (1, 5)], closed = True)
	ax.add_patch(square)
	#plt.show()

def draw_circles():
	y = 1.5
	while y < 5:
		x = 1.5
		while x < 5:
			c = draw_circle(x, y)
			ax = plt.gca()
			ax.add_patch(c)
			x += 1.0
		y += 1.0
	plt.show()


draw_square()
draw_circles()