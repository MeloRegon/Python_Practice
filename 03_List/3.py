from typing import Union

# Ask the user to enter numbers separated by spaces
numbers: str = input('Enter numbers: ')

# Split the string into a list of substrings
split_numbers: list[str] = numbers.split()

# Initialize an empty list
output: list[Union[int,str]] = []

for num in split_numbers:

    if int(num) % 2 == 0:
        output.append(int(num) * 2) # Double even numbers
    else:
        output.append('odd')

print(f'Output: {output}')