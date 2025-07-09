
# Ask the user to enter two numbers
first: int = int(input('Enter the first number: '))
second: int = int(input('Enter the second number: '))

# Compare the numbers
if first == second:
    print('Equal')
elif first > second:
    print('First is greater')
else:
    print('Second is greater')
