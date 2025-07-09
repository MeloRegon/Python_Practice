from itertools import count

# Ask the user to enter numbers separated by spaces
numbers: str = input('Enter numbers: ')

# Split the string into a list of substrings
split_numbers: list[str] = numbers.split()

# Initialize an empty list
output: list[int] = []

for num in split_numbers:
    if split_numbers.count(num) == 1:
        output.append(int(num))

print(f'Output: {output}')