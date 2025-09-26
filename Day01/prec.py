
x=10
y=x
print(x,y)
print(x is y)
print(id(x), id(y))


# immutable -> can not change the object(any change makes a new object)
# mutable -> object can change without creating a new one


# a="hi"
# print(id(a))
# a=a+" there"
# print(id(a))

# list

a = [1,2,3]
print(id(a))
b=a
print(id(b))
print(a is b)
b.copy()
b.append(4)
print(a)
print(b)
print(id(a),id(b))