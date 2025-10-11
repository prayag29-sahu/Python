from collections import Counter

nums = [1, 2, 2, 3, 3, 3, 4]
count = Counter(nums)
print(count.most_common(2))  # Top 2 most frequent
