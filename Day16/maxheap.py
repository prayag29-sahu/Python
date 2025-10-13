import heapq

nums = [4, 1, 7, 3, 8, 5]
max_heap = [-n for n in nums]
heapq.heapify(max_heap)

print("Max Heap:", [-n for n in max_heap])
heapq.heappush(max_heap, -10)
print("After push:", [-n for n in max_heap])

print("Max element popped:", -heapq.heappop(max_heap))
