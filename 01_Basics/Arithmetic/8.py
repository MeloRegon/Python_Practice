
for num in range(10, 100):
    digits: str = str(num)
    first: int = int(digits[0])
    second: int = int(digits[1])

    if second == first + 1:
        print(num)