n, a, b = map(int, input().split())
r1 = min(a, b)
r2 = max(a, b)
sum = 0

for i in range(1, n+1):
    temp = i
    value = 0
    while (temp > 0):
        value = value+(temp % 10)
        temp = temp//10
    if (r1 <= value <= r2):
        sum = sum+i
print(sum)


