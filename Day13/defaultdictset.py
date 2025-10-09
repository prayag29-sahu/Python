from collections import defaultdict

friends = defaultdict(set)
friends['Alice'].add('Bob')
friends['Alice'].add('Carol')
friends['Bob'].add('Alice')

print(dict(friends))
