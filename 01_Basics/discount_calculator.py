"""
Mini Project 01 - Basics

This script asks the user for the price of the product and the discount percentage,
and then displays the discount amount and the final price with the discount.
"""

price: float = float(input('Enter the price of the item: '))
discount: float = float(input('Enter the discount percentage: '))

total_discount: float = (price / 100) * discount
total_price: float = price - total_discount

print(f'\nDiscount: {total_discount}\n'
      f'Price after discount: {total_price}')