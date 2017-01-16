'''
3: Enhanced Unit Converter
The unit conversion program we wrote in this chapter is limited to conversions between kilometers and miles. Try extending the program to convert 
between units of mass (such as kilograms and pounds) and between units 
of temperature (such as Celsius and Fahrenheit).
'''

def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
    print('3. Kilograms to Pounds')
    print('4. Pounds to Kilograms')
    print('5. Celsius to Fahrenheit')
    print('6. Fahrenheit to Celsius')

def km_miles():
    km = float(input('Enter a distance in kilometers: '))
    miles = km / 1.609

    print('Distance in miles: {0:.2f}'.format(miles))

def miles_km():
    miles = float(input('Enter a distance in miles: '))
    km = miles * 1.609

    print('Distance in kilometers: {0:.2f}'.format(km))

def kg_pounds():
    kg = float(input('Enter the mass in kilograms: '))
    pounds = kg / 0.45359237;

    print('Mass in pounds: {0:.2f}'.format(pounds))

def pounds_kg():
    pounds = float(input('Enter the mass in pounds: '))
    kg = pounds * 0.45359237;

    print('Mass in pounds: {0:.2f}'.format(pounds))

def cel_fahr():
    celsius = float(input('Enter the temperature in Celsius: '))
    fahrenheit = celsius * (9 / 5) + 32;

    print('Temperature in Fahrenheit: {0:.2f}'.format(fahrenheit))

def fahr_cel():
    fahrenheit = float(input('Enter the temperature in Celsius: '))
    celsius = (fahrenheit - 32) * 5 / 9 ;

    print('Temperature in Fahrenheit: {0:.2f}'.format(celsius))
    
print_menu()
choice = input("Which conversion would you like to do?: ")
if choice == '1':
    km_miles()
elif choice == '2':
    miles_km()
elif choice == '3':
    kg_pounds()
elif choice == '4':
    pounds_kg()
elif choice == '5':
    cel_fahr()
elif choice == '6':
    fahr_cel()
