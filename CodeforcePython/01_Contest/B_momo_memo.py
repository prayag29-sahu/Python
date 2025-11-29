a,b,k = input().split()

a = int(a)
b = int(b)
k = int(k)

if(a%k == 0 and b%k == 0):
    print("Both")
elif(a%k ==0 and b%k!=0 ):
    print("Memo") 
elif(a%k!=0 and b%k == 0):
    print("Momo")
else:
    print("No One")
