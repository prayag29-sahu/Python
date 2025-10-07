from collections import namedtuple

Person = namedtuple('Person', ['name', 'age'])
p1 = Person(name='Alice', age=25)
print(p1)
print(p1.name, p1.age)
