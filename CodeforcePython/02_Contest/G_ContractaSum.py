t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    max_sum = n * (n + 1) // 2
    if s > max_sum:
        print(-1)
        continue
    result = []
    curr = s

    for num in range(n, 0, -1):
        if num <= curr:
            result.append(num)
            curr -= num
        if curr == 0:
            break
    print(*result)
