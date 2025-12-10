mystring='hello'
print(mystring)
mystring="hello"
print(mystring)
mystring='''hello'''
print(mystring)

print(mystring[0])
print(mystring[-1])
print(mystring[2:5])

# print(mystring[10])
# print(mystring[1.5])
# mystring[3]='f'

del mystring
# print(mystring)


s1="hello"
s2="python"
print(s1+s2)
print(s1*3)

count=0
for i in "hello python":
    if i=='o':
        count+=1;
print(count , "letter found")

print('l' in 'hello world')
print('o ' in 'hello world') 


print("hello".upper())
print("HELLO".lower())

print("hey i am python".split())
print(' '.join('hey' 'i' 'am' 'python'))

print("hey i am python".find('py'))

s1 = "bed morning"
s2 = s1.replace("bed","good")
print(s2)

palind1 = "acba"
p2 = reversed(palind1)

if list(palind1) == list(p2):
    print("Palindrom")
else:
    print("Not palindrom")

word = "python program for sort words in alphabetic order".split()
word.sort()

for w in word:
    print(w)
print(" ".join(word))

str1="  hello world  "
print(str1.strip())

str2="hello world"
print(str2.startswith("hello"))
print(str2.endswith("world"))
print(str2.count('o'))
print(str2.index('o'))
print(str2.capitalize())
print(str2.title())
print(str2.swapcase())
print(str2.center(50,'*'))
print(str2.zfill(30))
print(str2.islower())
print(str2.isupper())
print(str2.isalpha())
print(str2.isalnum())

print(str1.isalnum())
print(str1.isalpha())
print(str1.isupper())
print(str1.islower())
print(str1.zfill(30))
print(str1.center(50, '*'))
print(str1.swapcase())
print(str1.title())


