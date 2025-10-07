from collections import namedtuple

Student = namedtuple('Student', ['name', 'grade'])
s = Student('John', 'A')
print(s._asdict())
