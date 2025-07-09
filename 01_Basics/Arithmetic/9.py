

for num in range(10, 100):
    first: int = num // 10
    second: int = num % 10

    if (first + second) == (first * second):
        print(num)