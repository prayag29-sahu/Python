t = int(input())

for _ in range(t):
    n, s = map(int, input().split())

    if s > n*(n+1)//2:
        print(-1)
        continue
