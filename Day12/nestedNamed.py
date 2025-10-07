from collections import namedtuple

Address = namedtuple('Address', ['city', 'pincode'])
Person = namedtuple('Person', ['name', 'address'])

addr = Address('Delhi', 110001)
person = Person('Amit', addr)
print(person.address.city)
