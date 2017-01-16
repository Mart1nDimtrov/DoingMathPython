'''
2: Enhanced Multiplication Table Generator
Our multiplication table generator is cool, but it prints only the first 10 multiples. Enhance the generator so that the user can specify both the number 
and up to which multiple. For example, I should be able to input that I want 
to see a table listing the first 15 multiples of 9.
'''

def multi_table(a, b):

    for i in range(1, b + 1):
        print('{0} x {1} = {2}'.format(a, i, a*i))

        
a = input("Enter the number: ")
b = input("Enter the range: ")

multi_table(int(a), int(b))
