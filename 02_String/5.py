
# Convert input to lowercase to normalize comparison
sentence: str = input('Enter a text: ').lower()

# String to store unique characters in order
result = ""

# Iterate over each character in the sentence
for word in sentence:
    # Add character to result only if it hasn't appeared before
    if word not in result:
        result+= word

# Final print
print(result)