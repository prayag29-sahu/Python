A,S,B = input().split()
A = int(A)
B = int(B)
if(S==">"):
    if(A>B):
        print("Right")
    else:
        print("Wrong")
elif(S=="<"):
    if(A<B):
        print("Right")
    else:
        print("Wrong")
else:
    if(A==B):
        print("Right")
    else:
        print("Wrong")
