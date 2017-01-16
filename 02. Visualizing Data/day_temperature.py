'''
#1: How Does the Temperature Vary During the Day?
If you enter a search term like “New York weather” in Google’s search 
engine, you’ll see, ,ong other things, a graph showing the temperature 
at different times of the present day. Your task here is to re-create such a 
graph. 
Using a city of your choice, find the temperature at different points of 
the day. Use the data to create two lists in your progr, and to create a 
graph with the time of day on the x-axis and the corresponding temperature on the y-axis. The graph should tell you how the temperature varies 
with the time of day. Try a different city and see how the two cities compare 
by plotting both lines on the s,e graph.
The time of day may be indicated by strings such as '10:11 ,'or 
'09:21 PM'.
'''

import matplotlib.pyplot as plt

york_temp = [ 3.9,
4.7,
4.0,
4.2,
5.1,
5.4,
5.3,
5.7,
5.9,
5.1,
5.2  ]
sofia_temp = [ 0.2,
1.6,
1.2,
2.3,
3.5,
3.6,
0.2,
5.4,
0.5,
6.4,
3.5  ]

print(york_temp)
time = [x for x in range(0, len(york_temp))]
labels = [str(x) + ":00 AM" for x in range(0, len(york_temp))]

plt.plot(time, york_temp)
plt.plot(time, sofia_temp)
plt.title("Temperatures during the day")
plt.xlabel("Temperature")
plt.yticks(time, labels) # ticks as text must be a second argument
plt.legend(("New York", "Sofia")) # set the legend as a tuple
plt.axis([-1, 10, -1, 10])

plt.show()


