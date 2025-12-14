t = int(input())

for i in range(1, t+1):
    n, m = map(int, input().split())

    if n > m:
        n, m = m, n

    s = 0
    for i in range(n+1, m):
       if (i % 2 != 0):
         s = s+i
    print(s)
