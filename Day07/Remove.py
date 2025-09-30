
myset = {1, 2, 3, 4}

myset.remove(3)   # error if not present
myset.discard(10)  # no error if not present
print("After remove/discard:", myset)
