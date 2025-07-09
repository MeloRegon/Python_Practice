"""
Mini Project 01 - Basics

This script calculate simple interest and the total amount after a given time
based on user input: principal amount, annual interest rate, and time in years.
"""

principal: int = int(input('Enter the principal sum: '))
rate: float = float(input('Enter the annual interest rate (%): '))
time: int = int(input('Enter the time in years: '))

proc_sum: float = (principal * rate * time) / 100
total_sum: float = principal + proc_sum

print(f' Interest earned: {proc_sum}')
print(f'Total amount after {time} years: {total_sum}')