a,b,c,d = input().split()

a = int(a)
b = int(b)
c = int(c)
d = int(d)


if(a+b*c == d):
    print("YES")
elif(a+b-c == d):
    print("YES")    
elif(a-b+c == d):
    print("YES")    
elif(a-b*c == d):
    print("YES")    
elif(a*b-c == d):
    print("YES")    
elif(a*b+c == d):
    print("YES")    
else:
    print("NO")    



    