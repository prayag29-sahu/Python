import heapq

nums = [12, 3, 5, 7, 19]
k = 2
largest = heapq.nlargest(k, nums)
print(f"{k}th largest element:", largest[-1])
