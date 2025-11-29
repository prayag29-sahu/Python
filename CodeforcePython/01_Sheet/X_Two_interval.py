l1,r1,l2,r2 = input().split()

l1 = int(l1)
l2 = int(l2)
r1 = int(r1)
r2 = int(r2)

if(l1 > l2):
    i1 = l1
else:
    i1 = l2

if(r1 < r2):
    i2 = r1
else:
    i2 = r2

if(i1<=i2):
    print(i1,i2)
else :
    print("-1")
