from collections import Counter

text = "apple banana apple"
count = Counter(text.split())
print(dict(count))
# Output: {'apple': 2, 'banana': 1}