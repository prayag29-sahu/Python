import heapq

def heap_sort(nums):
    heapq.heapify(nums)
    return [heapq.heappop(nums) for _ in range(len(nums))]

arr = [7, 2, 5, 3, 1, 8]
print("Sorted:", heap_sort(arr))
