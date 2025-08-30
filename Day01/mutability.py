
# immutable -> can not change the object(any change makes a new object)
# mutable -> object can change without creating a new one


a="hi"
print(id(a))
a=a+" there"
print(id(a))
