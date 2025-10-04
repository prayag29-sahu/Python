matrix = [[1, 2, 3], [4, 5, 6]]
cols = len(matrix[0])
for j in range(cols):
    col_sum = sum(matrix[i][j] for i in range(len(matrix)))
    print(f"Column {j} Sum:", col_sum)
