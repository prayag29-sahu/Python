a=10
b=20

def add(a,b):
    return a+b  


def sub(a,b):       
    return a-b


def prod(a,b):
    return a*b


def div(a,b):
    return a/b

def power(a,b):
    return a**b

def root(a,b):
    return a**(1/b)

def calculator():
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Power")
    print("6.Root")

    choice = input("Enter choice(1/2/3/4/5/6): ")

    if choice in ['1', '2', '3', '4', '5', '6']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {sub(num1, num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {prod(num1, num2)}")

        elif choice == '4':
            print(f"{num1} / {num2} = {div(num1, num2)}")

        elif choice == '5':
            print(f"{num1} ^ {num2} = {power(num1, num2)}")

        elif choice == '6':
            print(f"{num2} root of {num1} = {root(num1, num2)}")
    else:
        print("Invalid Input")