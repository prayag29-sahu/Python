arr = bytearray(b'Python')
mv = memoryview(arr)
mv[0] = 106  # ASCII for 'j'
print(arr)
