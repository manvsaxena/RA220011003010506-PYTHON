print("Welcome to the Calculator! ")

print("Choose the operations : ")
print("+ - Addition ")
print("- - Substraction")
print("* - Multiplication")
print("/ - Division ")

op = input("Enter the operator: ")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if op == "+":
    print("Result: ")
    print(a+b)
elif op == "-":
    print("Result: ")
    print(a-b)
elif op == "*":
    print("Result: ")
    print(a*b)
elif op == "/":
    print("Result: ")
    print(a/b)