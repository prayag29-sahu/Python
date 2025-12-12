a, b = map(int, input().split())
count = 0
for i in range(a, b+1):
    num = str(i)
    lucky = True
    for j in range(0, len(num)):
        if (num[j] != '4' and num[j] != '7'):
            lucky = False
            break
    if (lucky == True):
        print(i, end=' ')
        count += 1
if count == 0:
    print("-1")
