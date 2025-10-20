def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "cmooon, you can't divide by zero!"

def calculator():
    print("You can perform the following operations:")
    print("a. Addition")
    print("b. Subtraction")
    print("c. Multiplication")
    print("d. Division")

    operation = input("Enter operation (a-d): ")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if operation == "a":
        print("Result:", add(a, b))
    elif operation == "b":
        print("Result:", subtract(a, b))
    elif operation == "c":
        print("Result:", multiply(a, b))
    elif operation == "d":
        print("Result:", divide(a, b))
    else:
        print("Invalid operation")

calculator()
