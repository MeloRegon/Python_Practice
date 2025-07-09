
# Ask the user to enter numbers separated by spaces
numbers: str = input('Enter numbers: ')

# Split the string into a list of integers
split_numbers: list[int] = [int(num) for num in numbers.split()]

# Calculate the sum of all numbers
output: int = sum(split_numbers)

print(f'Output: {output}')