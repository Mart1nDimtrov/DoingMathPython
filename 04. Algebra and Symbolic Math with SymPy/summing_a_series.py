'''
#3: Summing a Series
We saw how to find the sum of a series in “Printing a Series” on page 99. 
There, we manually added the terms of the series by looping over all the 
terms.
Your challenge is to write a program that’s capable of finding the sum 
of an arbitrary series when you supply the n th term of the series and the 
number of terms in it. Here’s an example of how the program would work:
Enter the n th term: a+(n-1)*d
Enter the number of terms: 3
3·a + 3·d
In this example, the n th term supplied is that of an arithmetic progression.
Starting with a and d as the common difference, the number of terms up 
to which the sum is to be calculated is 3. The sum turns out to be 3a + 3d, 
which agrees with the known formula for the same.
'''

from sympy import Symbol, summation, pprint

nth_term = input('Enter the nth term: ')
terms = input('Enter the number of terms: ')
x = Symbol('x')
n = Symbol('n')
s = summation(nth_term, (n, 1, terms)) 
pprint(s)

