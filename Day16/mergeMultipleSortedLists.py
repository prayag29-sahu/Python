import heapq

list1 = [1, 4, 7]
list2 = [2, 5, 8]
list3 = [3, 6, 9]
merged = list(heapq.merge(list1, list2, list3))
print("Merged sorted list:", merged)
