import math
A,B = map(int, input().split())
res = A/B

floor = math.floor(res)
ceil = math.ceil(res)
roun = math.floor(res+0.5)

print(f"floor {A} / {B} = {floor}")
print(f"ceil {A} / {B} = {ceil}")
print(f"round {A} / {B} = {roun}")
