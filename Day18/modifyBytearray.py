data = bytearray(b'python')
for i in range(len(data)):
    data[i] = data[i] - 32  # convert to uppercase ASCII
print(data.decode())
