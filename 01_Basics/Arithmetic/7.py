from collections import Counter


for num in range(100, 1000):
    digits: str = str(num)
    counts = Counter(digits)

    if len(counts) == 2 and sorted(counts.values()) == [1, 2]:
        print(num)