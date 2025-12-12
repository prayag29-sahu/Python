n = int(input())

if n <= 1:
    print("NO")

else:
    for i in range(2, n):
        if n % i == 0:
            print("NO")
            break
    else:
        print("YES")
