from collections import namedtuple

Car = namedtuple('Car', ['brand', 'model'])
data = ['Tesla', 'Model S']
car = Car._make(data)
print(car)
