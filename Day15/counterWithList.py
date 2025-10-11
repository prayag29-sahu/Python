from collections import Counter

words = ["cat", "dog", "cat", "lion", "dog", "cat"]
freq = Counter(words)
for word, count in freq.items():
    print(f"{word}: {count}")
