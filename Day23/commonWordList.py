l = ["hole", "whole", "goel", "tole", "sole"]

# Compare each word with every other word
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        w1 = l[i]
        w2 = l[j]
        # Find common letters using set intersection
        common_letters = set(word1) & set(word2)
        if common_letters:
            print(f"{word1} & {word2} → common letters: {', '.join(common_letters)}")
