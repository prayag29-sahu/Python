n = int(input())
A = list(map(int, input().split()))

min_val = min(A)

print(min_val, A.index(min_val)+1)

