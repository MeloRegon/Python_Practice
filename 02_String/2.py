
word: str = input('Enter a word: ')

if word.lower() == word[::-1].lower():
    print('True')
else:
    print('False')