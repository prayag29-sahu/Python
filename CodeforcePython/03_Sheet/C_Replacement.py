
n = int(input())
arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] > 0:
        arr[i] = 1
    elif arr[i] < 0:
        arr[i] = 2

for i in range(len(arr)):
    print(arr[i], end=" ")
