'''
#2: Law of Large Numbers
We’ve referred to a die roll and coin toss as two examples of random events 
that we can simulate using random numbers. We’ve used the term event 
to refer to a certain number showing up on a die roll or to heads or tails 
showing up on a coin toss, with each event having an associated probability 
value. In probability, a random variable—usually denoted by X—describes 
an event. For example, X= 1 describes the event of 1 appearing upon a die 
roll, and P(X= 1) describes the associated probability. There are two kinds 
of random variables: (1) discrete random variables, which take only integral 
values and are the only kind of random variables we see in this chapter, and 
(2) continuous random variables, which—as the name suggests—can take 
any real value.
The expectation, E, of a discrete random variable is the equivalent of the 
average or mean that we learned about in Chapter 3. The expectation can 
be calculated as follows:
E = x1*P(x1) +  x2*P(x2) +  x3*P(x3) + ... +  xn*P(xn)
According to the law of large numbers, the average value of results over 
multiple trials approaches the expected value as the number of trials 
increases. Your challenge in this task is to verify this law when rolling a 
six-sided die for the following number of trials: 100, 1000, 10000, 100000, 
and 500000.
'''

import random 

def roll_die(times):
	average = 0
	for roll in range(times):
		roll = random.randint(1, 6)
		average += roll*(1/6)
	return average/times*6


print("Expected value: 3.5")
times_array = [100, 1000, 10000, 100000]
e = 0
for times in times_array:
	e = roll_die(times)
	print("Trials: {0} Trial average {1:2f}".format(times, e))
