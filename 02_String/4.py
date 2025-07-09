from collections import Counter

# Convert input to lowercase to normalize comparison
sentence: str = input('Enter a text: ').lower()

# Filter only alphabetic characters
letters_only = [char for char in sentence if char.isalpha()]

counter = Counter(letters_only)

for letter, count in sorted(counter.items()):
    print(f'{letter}: {count}')
