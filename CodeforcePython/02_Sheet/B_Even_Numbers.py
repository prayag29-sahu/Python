a = int(input())

even = False

for i in range(2, a+1):
    if i % 2 == 0:
        print(i)
        even = True

if not even:
    print(-1)
