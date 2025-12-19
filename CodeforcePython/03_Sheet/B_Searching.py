n = int(input())
arr = list(map(int, input().split()))
x = int(input())

found = False

for i in range(n):
    if arr[i] == x:
        print(i)
        found = True
        break

if not found:
    print(-1)
