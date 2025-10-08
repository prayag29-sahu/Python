from collections import defaultdict

prices = defaultdict(lambda: "Not Available")
prices['apple'] = 100
print(prices['apple'])
print(prices['mango'])
