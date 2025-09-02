def func():
    pass
print(type(func()))
# <class 'NoneType'>

class demo:
    pass
print(type(demo()))
# <class '__main__.demo'>

# in python each and every thing is an object

""" Docstring for python which are accepted by compiler """

def add(a, b):
    """ This function is used to add two numbers """
    return a + b
print(add(10, 20 ))

# print docstring
help(add)

def factorial(n):
    """ This function is used to find the factorial of a number """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
# print docstring 
help(factorial)