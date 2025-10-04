arr = [1, 2, 3, 5, 6]
n = max(arr)
for i in range(1, n+1):
    if i not in arr:
        print("Missing:", i)
