import heapq

nums = [1, 3, 5, 7, 9, 2]
max_heap = []
for num in nums:
    heapq.heappush(max_heap, -num)
print("Max Heap built manually:", [-n for n in max_heap])

