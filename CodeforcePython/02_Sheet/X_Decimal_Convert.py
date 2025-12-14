t = int(input())
for i in range(0, t):
    n = int(input())
    lst = []
    while (n != 0):
        quotient = n//2
        remainder = n % 2
        n = quotient
        lst.append(remainder)
    binary = lst[::-1]
    count = binary.count(1)
    check = "1"*count
    sum = 0
    for j in check:
        value = int(2**(count-1))
        count = count-1

        sum = sum+value
    print(sum)
