"""
Mini Project 01 - Basics

This script converts a number of minutes into hours and minutes.
Useful for displaying time in a more readable format.
"""

minutes: int = int(input('Enter the number of minutes: '))
hours: int = minutes // 60
remaining_minutes: int = minutes % 60

print(f'{minutes} minutes = {hours} hours and {remaining_minutes} minutes')