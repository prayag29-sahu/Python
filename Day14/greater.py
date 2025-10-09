# a = 5
# b=34
# c=32

a,b,c = input("Enter 3 numbers : ").split()

if(a>b and a>c):
    print(a)
elif(b>a and b>c):
    print(b)
elif(c>a and c>b):
    print(c)    