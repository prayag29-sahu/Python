from collections import Counter

c = Counter("apple")
c.update("banana")  # adds counts
print(c)
# Counter({'a': 4, 'p': 2, 'n': 2, 'l': 1, 'e': 1, 'b': 1})