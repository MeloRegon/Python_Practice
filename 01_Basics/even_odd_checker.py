"""
Mini Project 01 - Basics

this script checks whether a given number is Even or Odd
based on user input.
"""

num: int = int(input('Enter a number: '))

if num % 2 == 0:
    print('The number is Even.')
else:
    print('The number is Odd.')