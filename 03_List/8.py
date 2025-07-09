
# Ask the user to enter numbers separated by spaces
numbers: str = input('Enter numbers: ')

# Split the string into a list of integers
split_numbers: list[int] = [int(num) for num in numbers.split()]

# Initialize a variable to store the product of add numbers
output: int = 1

for num in split_numbers:
    if num % 2 != 0:
        output *= num

print(f'Output: {output}')