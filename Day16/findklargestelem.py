import heapq

nums = [15, 3, 9, 8, 20, 12]
k = 2
print(f"{k} largest elements:", heapq.nlargest(k, nums))
