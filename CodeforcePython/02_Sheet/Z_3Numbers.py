k, s = map(int, input().split())

count = 0
for x in range(0, k + 1):
    remaining = s - x
    if remaining < 0:
        continue

    low = max(0, remaining - k)
    high = min(k, remaining)

    if low <= high:
        count += (high - low + 1)

print(count)