from typing import NamedTuple


class Laptop(NamedTuple):
    brand: str
    price: int
    ram: int


l1 = Laptop('HP', 55000, 16)
print(l1)
