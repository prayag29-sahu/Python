import math
a,b,c,d = input().split()

a = int(a)
b = int(b)
c = int(c)
d = int(d)
res = b*math.log(a)
res1 = c*math.log(d)
if(res > res1):
    print("YES")
else:
    print("NO")