from collections import defaultdict


def tree(): return defaultdict(tree)


data = tree()

data['India']['Maharashtra']['Pune'] = "Beautiful City"
print(data['India']['Maharashtra']['Pune'])
