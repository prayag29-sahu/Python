from collections import defaultdict

text = "banana"
count = defaultdict(int)

for ch in text:
    count[ch] += 1

print(dict(count))
