a = 121

pal = lambda a: print(palindrome(a))

def palindrome(n):
    b = n
    rev = 0
    while n > 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10
    return rev == b

pal(a)  
