
from collections import Counter

# Ask the user to enter a sentence
sentence: str = input('Enter a text: ').lower()

# Filter only alphabetic characters
letters_only = [char for char in sentence if char.isalpha()]

# Counter frequency of each letter
counter = Counter(letters_only)

# Get top 3 most common letters
top_3 = counter.most_common(3)

# Display result
for char,freq in top_3:
    print(f'{char}: {freq}')