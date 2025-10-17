arr = bytearray(b'python')
mv = memoryview(arr)
mv[0:2] = b'Py'
print(arr)
