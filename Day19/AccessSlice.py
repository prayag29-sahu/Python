data = bytearray(b'HELLO')
mv = memoryview(data)
sub = mv[1:4]
print(sub.tobytes())
