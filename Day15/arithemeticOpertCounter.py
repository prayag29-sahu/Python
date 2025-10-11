from collections import Counter

a = Counter(A=4, B=2, C=0)
b = Counter(A=1, B=2, D=3)
print(a + b)  # addition
print(a - b)  # subtraction (no negatives)
