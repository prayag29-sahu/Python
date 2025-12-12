n = input().strip()

rev = n[::-1].lstrip('0')
print(rev)

if n == n[::-1]:
    print("YES")
else:
    print("NO")
