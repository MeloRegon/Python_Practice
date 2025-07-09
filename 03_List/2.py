
# Ask the user to enter numbers separated by spaces
numbers: str = input('Enter numbers: ')

# Split the string into a list of substrings
split_numbers: list[str] = numbers.split()

# Initialize an empty list
output: list[int] = []

for num in split_numbers:
    output.append(int(num) * 2)

print(f'Output: {output}')