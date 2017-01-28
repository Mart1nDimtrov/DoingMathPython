from sympy import FiniteSet

s = FiniteSet(1, 2)
t = FiniteSet(3, 4)
p = s*t

for elem in p:
	print(elem)

print('The cardinality of the Cartesan product is {0}'.format(len(p)))