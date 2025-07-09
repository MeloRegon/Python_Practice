# File Reader Utility
# Prompts the user for a file name and displays its contents.
# Catches and handles FileNotFoundError.

try:
    file_name = input('Enter the file name: ')
    with open(file_name, 'r') as file:
        content = file.read()
        print('\nFile Content:\n')
        print(content)

except FileNotFoundError:
    print('File not found. Please check the file name and try again.')