'''
#2: Drawing the Sierpin´  ski Triangle
The Sierpin´  ski triangle, named after the Polish mathematician Wacław 
Sierpin´  ski, is a fractal that is an 
equilateral triangle composed of smaller 
equilateral triangles embedded inside it. 
Each of the transformations has an equal probability of being 
selected—1/3. Your challenge here is to write a program that draws the 
Sierpin´  ski triangle composed of a 
certain number of points specified as 
input. 
'''
import random
import matplotlib.pyplot as plt

def transformation_1(p):
	x = p[0]
	y = p[1]
	x1 = 0.5*x 
	y1 = 0.5*y
	return x1, y1

def transformation_2(p):
	x = p[0]
	y = p[1]
	x1 = 0.5*x + 0.5
	y1 = 0.5*y + 0.5
	return x1, y1

def transformation_3(p):
	x = p[0]
	y = p[1]
	x1 = 0.5*x + 1
	y1 = 0.5*y
	return x1, y1


def get_index(probability):
	r = random.random()
	c_probability = 0
	sum_probability = []
	for p in probability:
		c_probability += p
		sum_probability.append(c_probability)
	for item, sp in enumerate(sum_probability):
		if r <= sp:
			return item
	return len(probability)-1

def transform(p):
	# List of transformation functions
	transformations = [transformation_1, transformation_2, 
		transformation_3]
	probability = [1/3, 1/3, 1/3]
	# Pick a random transformation function and call it
	tindex = get_index(probability)
	t = transformations[tindex]
	x, y = t(p)
	return x, y

def draw_fern(n):
	# We start with (0, 0)
	x = [0]
	y = [0]
	x1, y1 = 0, 0
	for i in range(n):
		x1, y1 = transform((x1, y1))
		x.append(x1)
		y.append(y1)
	return x, y


n = int(input('Enter the number of points in the Triangle: '))
x, y = draw_fern(n)
# Plot the points
plt.plot(x, y, 'o')
plt.title('Triangle with {0} points'.format(n))
plt.savefig('sierpinski_triangle.png')
plt.show()
