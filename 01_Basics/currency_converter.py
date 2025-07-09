"""
Mini Project 01 - Basics

This script asks the user for the amount in euros and the exchange rate to dollars,
then displays the result in dollars.
"""

eur_sum: float = float(input('Enter amount in EUR: '))
exchange_rate: float = float(input('Enter exchange rate (EUR to USD): '))

total_sum: float = round(eur_sum * exchange_rate, 2)

print(f'{eur_sum} EUR is equal to {total_sum} USD')