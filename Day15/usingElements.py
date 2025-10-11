from collections import Counter

c = Counter(a=3, b=1)
print(list(c.elements()))
#  ['a', 'a', 'a', 'b']