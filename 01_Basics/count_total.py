"""
Mini Project 01 - Basics

This script calculates the total price for a given number of items
including tax percentage.
"""

# Input section: read price, quantity, and tax rate from user input
price: int = int(input('Enter the item price: '))
total_item: int = int(input('Enter the quantity of items: '))
tax: float = float(input('Enter the tax (%): '))

# Calculate total price without tax
final_summ: int = price * total_item

# Calculate total price with tax
final_summ_with_tax: float = final_summ + ((final_summ / 100) * tax)

# Output results
print(f'The Final summ without TAX: {final_summ}')
print(f'The Final sum with TAX: {final_summ_with_tax:.2f}')