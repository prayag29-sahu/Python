from collections import Counter

text = "banana"
c = Counter(text)
filtered = {k: v for k, v in c.items() if v > 1}
print(filtered)
#  {'a': 3, 'n': 2}