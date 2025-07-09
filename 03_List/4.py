
# Ask the user to enter numbers separated by spaces
numbers: str = input('Enter numbers: ')

# Split the string into a list of integers
split_numbers: list[int] = [int(num) for num in numbers.split()]

# Find the max and min numbers
max_output: int = max(split_numbers)
min_output: int = min(split_numbers)

print(f'Max: {max_output}\n'
      f'Min: {min_output}')



