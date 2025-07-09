import string
from string import punctuation

# Ask the user to enter a sentence
sentence: str = input('Enter a text: ')

# Get all punctuation characters
punctuations = string.punctuation

# Remove punctuation
cleaned: str = "".join(char for char in sentence if char not in punctuations)

print(cleaned)

