num=12345
sum=0
count=0
while num>0:
    if num%2==0:
        count=count+1
        sum+=num%10
    num=num//10
print(sum)
print(count)
