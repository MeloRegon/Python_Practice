
# Ask the user to enter a sentence
sentence: str = input('Enter a text: ')

# Split the sentence into words
words = sentence.split()

# Count the number of words
count = len(words)

print(f'Word count {count}')