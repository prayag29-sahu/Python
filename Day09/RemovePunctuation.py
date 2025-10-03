import string
text = "Hello, World! Welcome to Python."
cleaned = "".join(ch for ch in text if ch not in string.punctuation)
print(cleaned)
