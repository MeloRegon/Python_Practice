

# Convert input to lowercase to normalize comparison
sentence: str = input('Enter a text: ').lower()

# Split the sentence into words
words: list[str] = sentence.split()

# Capitalize each word and store in a new list
capitalized_words: list[str] = [word.capitalize() for word in words]

# Join the words back into a sentence with spaces
result: str = " ".join(capitalized_words)

print(result)