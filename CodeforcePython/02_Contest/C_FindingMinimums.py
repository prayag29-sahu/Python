N, K = map(int, input().split())
a = list(map(int, input().split()))

for i in range(0, N, K):
    print(min(a[i:i+K]), end=" ")
