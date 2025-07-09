
first_num: int = int(input('Enter the first number: '))
second_num: int = int(input('Enter the second number: '))

quotient: int = first_num // second_num
remainder: int = first_num % second_num

print(f'\nQuotient: {quotient}\n'
      f'Remainder: {remainder}')

if first_num % second_num !=0:
    print(f'{first_num} is not a multiple of {second_num}')
else:
    print(f'{first_num} is a multiple of {second_num}')

    