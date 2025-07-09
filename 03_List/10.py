

# Ask the user to enter numbers separated by spaces
numbers: str = input('Enter numbers: ')

# Split the string into a list of integers
split_numbers: list[int] = [int(num) for num in numbers.split()]

# Find the max and min numbers
max_output: int = max(split_numbers)
min_output: int = min(split_numbers)

# Remove the first occurrence of the mon and max values
split_numbers.remove(min_output)
split_numbers.remove(max_output)

print(f'Output: {split_numbers}')