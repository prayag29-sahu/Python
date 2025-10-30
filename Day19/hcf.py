def hcf(x, y):

    min = x if x<y else y
    hcf = 1
    for i in range(1, min+1):
        if x%i == 0 and y%i == 0:
            hcf = i
    return hcf

def lcm(x,y):
    max = x if x>y else y
    while True:
        if max%x==0 and max%y==0:
            return max
        max+=1


a = int(input())
b = int(input())
print(hcf(a, b))
lcm = lcm(a,b)
print(lcm)