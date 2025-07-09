
# Ask the user to enter a sentence
sentence: str = input('Enter a text: ')

# Split the sentence into words
words = sentence.split()

# Reverse each word
reversed_words = [word[::-1] for word in words]

# Join the reversed words back into a sentence
result = " ".join(reversed_words)

print(result)