from collections import deque
dq = deque([1, 2, 3, 4])
dq.pop()             # Removes 4
dq.popleft()         # Removes 1
print(dq)            # Output: deque([2, 3])
