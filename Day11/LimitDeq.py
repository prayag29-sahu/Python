from collections import deque
dq = deque(maxlen=3)
dq.extend([1, 2, 3])
dq.append(4)          # Oldest (1) is dropped
print(dq)             # Output: deque([2, 3, 4], maxlen=3)
