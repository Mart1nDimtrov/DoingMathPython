'''
5: Give Exit Power to the User
All the programs we have written so far work only for one iteration of input 
and output. For example, consider the program to print the multiplication 
table: the user executes the program and enters a number; then the program prints the multiplication table and exits. If the user wanted to print 
the multiplication table of another number, the program would have to be 
rerun.
Try rewriting some of the other programs in this chapter so that they 
continue executing until asked by the user to exit.
'''

def multi_table(a, b):

    for i in range(1, b + 1):
        print('{0} x {1} = {2}'.format(a, i, a*i))

while(True):
    a = input("Enter the number: ")
    b = input("Enter the range: ")
    multi_table(int(a), int(b))

    answer = input("\nDo you want to exit? Type (y) for yes ").lower()
    if answer == 'y':
        break


