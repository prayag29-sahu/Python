import heapq

nums = [9, 4, 7, 1, 3, 6, 8, 2]
k = 3
print(f"{k} smallest elements:", heapq.nsmallest(k, nums))
