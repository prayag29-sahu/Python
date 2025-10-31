from collections import deque
dq = deque([1,2,3])
dq.appendleft(0)
print(dq)
dq.append(4)
dq.pop()
print(dq)