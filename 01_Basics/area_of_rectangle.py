"""
Mini Project 01 - Basics

This script calculate the area and perimeter of a rectangle
based on user input: width and length.
"""

width: float = float(input('Enter the rectangle width: '))
length: float = float(input('Enter the rectangle length: '))

area: float = width * length
perimeter: float = 2 * (width + length)

print(f'The area of the rectangle: {area}\n'
    f'The perimeter of the rectangle: {perimeter}')

