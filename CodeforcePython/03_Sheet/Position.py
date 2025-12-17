
n = int(input())

A = list(map(int, input().split()))

for i in range(len(A)):
    if A[i] <= 10:
        print(f"A[{i}] = {A[i]}")
