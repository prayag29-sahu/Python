l = [1,2,0,3,2,0,6,0,0,4,2]

Z=0
out=[]
for i in l:
    if i!=0:
        out.append(i)
    else:
        Z+=1


for j in range(Z):
    out.append(0)   
print(out)