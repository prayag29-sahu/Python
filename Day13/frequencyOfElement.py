from collections import defaultdict

numbers = [1, 2, 2, 3, 3, 3]
freq = defaultdict(int)

for n in numbers:
    freq[n] += 1

print(dict(freq))
