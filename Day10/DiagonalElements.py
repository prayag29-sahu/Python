matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
n = len(matrix)
primary = [matrix[i][i] for i in range(n)]
secondary = [matrix[i][n-i-1] for i in range(n)]
print("Primary Diagonal:", primary)
print("Secondary Diagonal:", secondary)
