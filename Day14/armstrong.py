a=153
b=0
c=a
while a>0:
    r=a%10
    b=r**3+b
    a=a//10

if b==c:
    print("armstrong")
else:
    print("not armstrong")