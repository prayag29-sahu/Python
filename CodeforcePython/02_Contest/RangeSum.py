t = int(input())

for _ in range(t):
    l, r = map(int, input().split())

    if l > r:
        l, r = r, l   # swap

    ans = (r*(r+1))//2 - (l*(l-1))//2
    print(ans)
