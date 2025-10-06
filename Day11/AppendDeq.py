from collections import deque

dq = deque([2, 3])
dq.append(4)         # Add to right
dq.appendleft(1)     # Add to left
print(dq)            # Output: deque([1, 2, 3, 4])
