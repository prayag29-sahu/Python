arr = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        for k in range(len(arr[i][j])):
            print(f"arr[{i}][{j}][{k}] = {arr[i][j][k]}")
