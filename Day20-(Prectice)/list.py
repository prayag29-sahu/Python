fruits = ["apple", "banana", "mango"]
print(fruits)


# access element 
print(fruits[1])  # banana

# append element
fruits.append("orange")

# insert element
fruits.insert(1, "grape")

# remove element
fruits.remove("mango")

# pop element
popped_fruit = fruits.pop()  # removes last element

# slicing
print(fruits[1:3])  # gets elements from index 1 to