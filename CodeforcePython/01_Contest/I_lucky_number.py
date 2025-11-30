a = int(input())

b=a%10;
r=int(a/10);

if b%r==0 or r%b==0:
    print("YES")
else :
    print("NO")

