"""
Mini Project 01 - Basics

This script determines whether the entered year is a leap year.
"""

year: int = int(input('Enter a year: '))

if year % 400 == 0:
    print(f'The year {year} is a leap year')
elif year % 100 == 0:
    print(f'The year {year} is not a leap year')
elif year % 4 == 0:
    print(f'The year {year} is a leap year')
else:
    print(f'The year {year} is not a leap year')