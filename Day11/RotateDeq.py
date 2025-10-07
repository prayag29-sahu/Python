from collections import deque

dq = deque([1, 2, 3, 4])
dq.rotate(1)         # Rotate right: deque([4, 1, 2, 3])
dq.rotate(-2)        # Rotate left: deque([2, 3, 4, 1])
print(dq)
