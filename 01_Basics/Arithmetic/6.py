


for num in range(100, 1000):
    first = num // 100
    middle = (num // 10) % 10
    last = num % 10

    if first == last and (first + middle + last) % 5 == 0:
        print(num)