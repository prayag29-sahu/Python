A, S, B, t, d = input().split()
A = int(A)
d = int(d)
B = int(B)
if (S == "+"):
    if (A+B == d):
        print("Yes")
    else:
        print(A+B)
elif (S == "*"):
    if (A*B == d):
        print("Yes")
    else:
        print(A*B)
elif (S == '-'):
    if (A-B == d):
        print("Yes")
    else:
        print(A-B)
