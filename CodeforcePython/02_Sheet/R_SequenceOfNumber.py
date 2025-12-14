while True:
    n, m = map(int, input().split())

    if n <= 0 or m <= 0:
        break

    if n > m:
        n, m = m, n

    s = 0
    for i in range(n, m+1):
        print(i, end=" ")
        s = s+i
    print(f"sum ={s}")
