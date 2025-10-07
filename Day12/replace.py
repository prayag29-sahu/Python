from collections import namedtuple

Book = namedtuple('Book', ['title', 'author'])
b = Book('Python 101', 'Guido')
new_b = b._replace(author='Rossum')
print(new_b)
