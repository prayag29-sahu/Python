import heapq

nums = [5, 3, 8, 1, 2]
heapq.heapify(nums)
print("Min Heap:", nums)

heapq.heappush(nums, 0)
print("After push:", nums)

