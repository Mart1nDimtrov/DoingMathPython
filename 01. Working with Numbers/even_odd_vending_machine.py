'''
1: Even-Odd Vending Machine
Try writing an “even-odd vending machine,” which will take a number as 
input and do two things:
1.  Print whether the number is even or odd.
2.  Display the number followed by the next 9 even or odd numbers.
If the input is 2, the program should print even and then print 2, 4, 6, 
8, 10, 12, 14, 16, 18, 20. Similarly, if the input is 1, the program should 
print odd and then print 1, 3, 5, 7, 9, 11, 13, 15, 17, 19. 
Your program should use the is_integer() method to display an error 
message if the input is a number with significant digits beyond the decimal 
point.
'''

def even_odd(number):
    if (number % 2 == 0):
        print("The number is even")
    else:
        print("The number is odd")

    for i in range(number, number + 20, 2):
        print(i)

number = float(input("Please an integer number: "))
if (number.is_integer()):
    even_odd(int(number))
else:
    print("Please enter a vild number.")


    
