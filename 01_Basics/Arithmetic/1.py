


for num in range(1001):
    if num % 3 == 0 and num % 5 != 0 and sum(int(d) for d in str(num)) < 10:
        print(num)

