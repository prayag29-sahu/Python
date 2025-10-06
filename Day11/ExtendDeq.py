from collections import deque
dq = deque([3, 4])
dq.extend([5, 6])         # Extend right
dq.extendleft([2, 1])     # Extend left (adds in reverse order)
print(dq)                 # Output: deque([1, 2, 3, 4, 5, 6])
