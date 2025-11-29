s,d,r,c = input().split() 
s = int(s)
r = int(r)
d = int(d)
c = int(c)
a = s*c*r*d
a=a%100
print(f"{a:02d}")