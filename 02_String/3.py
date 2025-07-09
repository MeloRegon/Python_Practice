
sentence: str = input('Enter a sentence: ')
words = sentence.split()

longest = max(words, key=len)

print(f'Longest word: {longest}')