"""
Mimi Project 01_Basics

This script converts temperatures between Celsius and Fahrenheit
based on user input.
"""


question: str = input('Enter conversion type (CtoF or FtoC): ').lower()
temp: int = int(input('Enter the temperature: '))


if question == 'ctof':
    result = (temp * (9 / 5)) + 32
    print(f'Temperature in Fahrenheit: {result}')
elif question == 'ftoc':
    result = (temp - 32) * (5 / 9)
    print(f'Temperature in Celsius: {result}')

else:
    print("Type Error: Please enter 'Ctof' or 'FtoC' ")