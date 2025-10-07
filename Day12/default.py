from collections import namedtuple

Employee = namedtuple('Employee', ['name', 'salary', 'department'])
Employee.__new__.__defaults__ = (50000, 'General')
e = Employee('Bob')
print(e)
