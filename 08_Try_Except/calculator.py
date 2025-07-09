# Simple Arithmetic Calculator
# Performs basic operations (+, -, *, /) between two numbers.
# Handles input errors and division by zero.

import sys

try:
    first_num = float(input('Enter the first number: '))
    second_num = float(input('Enter the second number: '))
    operation = input('Enter operation (+, -, *, /): ')

    if operation == '+':
        result = first_num + second_num
    elif operation == '-':
        result = first_num - second_num
    elif operation == '*':
        result = first_num * second_num
    elif operation == '/':
        if second_num == 0:
            print('Cannot divide by zero')
            sys.exit()
        result = first_num / second_num
    else:
        print('Unknown operation')
        sys.exit()

    print('Result:', result)

except ValueError:
    print('Invalid input. Please enter numeric values.')
