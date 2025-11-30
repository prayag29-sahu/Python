n = int(input())
l = list(map(int, input().split()))

e=0
o=0
p=0
n=0
for i in l:
    if i % 2 == 0:
        e += 1
    else:
        o += 1
    
    if i > 0:
        p += 1
    elif i < 0:
        ne += 1


# print(list)        
print("Even: ",e)
print("Odd: ",e)
print("Positive: ",e)
print("Negative: ",e)

