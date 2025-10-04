arr = [10, 40, 30, 20, 50]
arr = list(set(arr))  # remove duplicates
arr.sort()
print("Second Largest:", arr[-2])
