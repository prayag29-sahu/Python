arr = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
total = sum(sum(sum(layer) for layer in arr[i]) for i in range(len(arr)))
print("Sum of all elements:", total)
