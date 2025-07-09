"""
Mini Project 01 - Basics

This script calculate the area and circumference of a circle
based on user input: radius
"""

import math

radius: float = float(input('Enter the circle radius: '))

area: float = round(math.pi * (radius ** 2), 2)
circumference: float = round( 2 * math.pi * radius, 2)

print(f'\nThe circle area: {area}\n'
      f'The circle circumference: {circumference}')
