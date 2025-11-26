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