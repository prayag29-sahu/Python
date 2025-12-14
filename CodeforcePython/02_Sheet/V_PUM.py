n = int(input())
x = 1

for i in range(n):
    for j in range(3):
        print(x, end=" ")
        x += 1
    print("PUM")
    x += 1
