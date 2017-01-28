'''
#1: Using Venn Diagrams to Visualize Relationships Between Sets
Draw a Venn diagram for two sets
'''
import csv
from matplotlib_venn import venn2
import matplotlib.pyplot as plt
from sympy import FiniteSet

def draw_venn(s1, s2): # pass them as seperate lists and include each in a set
	venn2([set(s1), set(s2)])
	plt.show()

def read_csv(filename):
	football = [] 
	others = [] 
	with open(filename) as f:
		reader = csv.reader(f)
		next(reader)
		for row in reader:
			if row[1] == '1': 
				football.append(row[0])
			if row[2] == '1':
				others.append(row[0])
	return football, others


filename = "students.csv"
s1, s2 = read_csv(filename)
draw_venn(s1, s2)