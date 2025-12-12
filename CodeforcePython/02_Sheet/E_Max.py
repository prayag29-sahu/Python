n = int(input())
arr = list(map(int, input().split()))

max = 0

for i in arr:
    if max < i:
        max = i
print(max)
