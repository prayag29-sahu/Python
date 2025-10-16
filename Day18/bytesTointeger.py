num = 1024
byte_data = num.to_bytes(2, 'big')
print(byte_data)

restored = int.from_bytes(byte_data, 'big')
print(restored)
print(restored == num)