
a,b,c = input().split()

n=int(a)
m=int(b)
k=int(c)

u_m = min(n,m,k)

n-=u_m
m-=u_m
k-=u_m

num_mouth = min(n//2,k)

print(u_m+num_mouth)

