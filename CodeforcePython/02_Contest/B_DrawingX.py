n = int(input())
m = n // 2
for i in range(n):
    for j in range(n):
        if i == m and j == m:
            print("X", end="")
        elif i == j:
            print("\\", end="")
        elif i + j == n - 1:
            print("/", end="")
        else:
            print("*", end="")
    print()


