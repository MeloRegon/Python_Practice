

# Ask the user to enter numbers separated by spaces
numbers: str = input('Enter numbers: ')

# Split the string into a list of integers
split_numbers: list[int] = [int(num) for num in numbers.split()]

# Initialize an empty list
output: list[int] = []

# Loop through the lit and add only unique numbers

for num in split_numbers:
    if num not in output:
        output.append(num)

print(f'Output: {output}')