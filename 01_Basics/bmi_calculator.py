"""
Mini Project 01 - Basics

The script calculates the Body Mass Index (BMI)
based on user's height (in cm) and weight (in kg).
"""

weight: int = int(input('Enter your weight in kg: '))
height: int = int(input('Enter your height in cm: '))


if height == 0 or weight == 0:
    print('Height or Weight cannot be zero.')
else:
    total_bmi = round((weight / (height ** 2)) * 10000, 2)
    print(f'Your BMI is {total_bmi}')