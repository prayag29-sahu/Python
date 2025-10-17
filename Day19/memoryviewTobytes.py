arr = bytearray(b'abcde')
mv = memoryview(arr)
b = mv.tobytes()
print(b)
