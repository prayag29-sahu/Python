from collections import defaultdict

data = [('fruit', 'apple'), ('fruit', 'banana'), ('veg', 'carrot')]
combined = defaultdict(list)

for k, v in data:
    combined[k].append(v)

print(dict(combined))
