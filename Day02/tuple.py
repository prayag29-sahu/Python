a = 10
b = "10"
c = a, b
print(a)
print(b)
print(c)
print(type(c))
# 10
# 10
# (10, '10')
# <class 'tuple'>
# Creating a tuple
my_tuple = ("apple", "banana", "cherry")

print("First fruit:", my_tuple[0])  # Output: apple

for fruit in my_tuple:
    print("Fruit:", fruit)
