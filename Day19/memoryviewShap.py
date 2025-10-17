import array
a = array.array('i', [10, 20, 30])
mv = memoryview(a)
print(mv.format)
print(mv.shape)
