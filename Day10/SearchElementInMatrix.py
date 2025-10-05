matrix = [[10, 20, 30],
          [40, 50, 60],
          [70, 80, 90]]

x = 50
found = False
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == x:
            print(f"Found {x} at ({i}, {j})")
            found = True
if not found:
    print("Not Found")
