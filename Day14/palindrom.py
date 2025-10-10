a=121
b=0
c=a
while a>0:
    r=a%10
    b=b*10+r
    a=a//10

if b==c:
    print("palindrome")
else:
    print("not palindrome")