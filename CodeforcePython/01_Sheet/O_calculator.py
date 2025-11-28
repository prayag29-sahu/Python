s = input().strip()

if '+' in s:
    A, B = s.split('+')
    print(int(A) + int(B))
elif '-' in s:
    A, B = s.split('-')
    print(int(A) - int(B))
elif '*' in s:
    A, B = s.split('*')
    print(int(A) * int(B))
elif '/' in s:
    A, B = s.split('/')
    print(int(A) // int(B))
