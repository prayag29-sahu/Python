n, k, a = map(int, input().split())

INT_MIN = -2147483648
INT_MAX = 2147483647
LL_MIN = -9223372036854775808
LL_MAX = 9223372036854775807

d = n * k

if d % a != 0:
    print("double")

else:
    val = d // a
    
    if INT_MIN <= val <= INT_MAX:
        print("int")
    elif LL_MIN <= val <= LL_MAX:
        print("long long")
    else:
        print("double") 
