"""
Mini Project 01 - Basics

This script calculates the average value of the subjects entered by the user.
"""

# Input: number of subjects
subject_count: int = int(input('Enter the number of subjects: '))
grade_summ = 0

# Collect grades using a loop
for i in range(1, subject_count + 1):
    grade: int = int(input(f'Enter grade for subject {i}: '))
    grade_summ += grade

# Calculate average
average_value = round(grade_summ / subject_count, 2)

# Output result
print(f'The average grade is {average_value}')


