from collections import namedtuple

Fruit = namedtuple('Fruit', ['name', 'color', 'price'])
apple = Fruit('Apple', 'Red', 120)

for field in apple:
    print(field)
