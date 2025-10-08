from collections import defaultdict

d = defaultdict(int)
print(d['missing'])  # returns 0, not KeyError
