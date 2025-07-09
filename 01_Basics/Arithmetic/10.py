

for num in range(100, 1000):
    digits: str = str(num)

    if '0' not in digits and int(digits) % 3 == 0 and len(set(digits)) == 3:
        print(num)