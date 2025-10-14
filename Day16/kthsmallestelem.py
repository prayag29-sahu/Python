import heapq

nums = [12, 3, 5, 7, 19]
k = 2
heapq.heapify(nums)
for _ in range(k-1):
    heapq.heappop(nums)
print(f"{k}th smallest element:", heapq.heappop(nums))
