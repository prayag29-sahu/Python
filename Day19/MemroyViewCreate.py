data = bytes([10, 20, 30, 40, 50])
mv = memoryview(data)
print(mv)
print(mv.tolist())
