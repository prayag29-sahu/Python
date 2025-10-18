import array
a = array.array('h', [100, 200, 300])  # 'h' = short
mv = memoryview(a)
mv[1] = 999
print(a)
