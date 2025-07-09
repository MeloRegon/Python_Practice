
sentence: str = input('Enter a sentence: ')
words = sentence.split()

vowels = 'aeiouy'
found = False

for word in words:
    if all(letter.lower() in vowels for letter in word):
        print(word)
        found = True

if not found:
    print('No words with only vowels.')


