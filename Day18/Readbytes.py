with open("example.txt", "wb") as f:
    f.write(b"Binary data test")

with open("example.txt", "rb") as f:
    content = f.read()
    print(content)
