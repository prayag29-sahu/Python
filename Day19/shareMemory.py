arr = bytearray(b'world')
mv = memoryview(arr)
arr[0] = ord('W')
print(mv.tobytes())
