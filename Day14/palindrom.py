# a=121
# b=0
# c=a
# while a>0:
#     r=a%10
#     b=b*10+r
#     a=a//10

# if b==c:
#     print("palindrome")
# else:
#     print("not palindrome")

n=12321
if str(n)[::-1]==str(n):
    print("palindrome")
else:
    print("not palindrome")    