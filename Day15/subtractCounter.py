from collections import Counter

x = Counter(a=5, b=2)
y = Counter(a=3, b=5)
x.subtract(y)
print(x)
# Counter({'a': 2, 'b': 1})