
a=10
b=50
print("Prime numbers between",a,"and",b,"are:")

for i in range(a,b+1):
    prime = True
    if i < 2:
        prime = False
    else:
        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
    if prime:
        print(i)
