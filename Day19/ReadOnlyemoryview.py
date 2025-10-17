data = bytes([1, 2, 3, 4])
mv = memoryview(data)
print(mv.readonly)
