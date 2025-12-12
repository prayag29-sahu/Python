t = int(input())

for _ in range(t):
    n = input().strip()
    for i in n[::-1]:
        print(i, end=" ")
    print()
