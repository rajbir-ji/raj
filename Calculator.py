a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
def add(a,b):
    return a + b
def sub(a,b):
    return a - b    
def mul(a,b):
    return a * b
def div(a,b):
    return a / b
print("Calculator module imported")
print("Enter your choice of operation :+,-,*,/")
ch=input()
if ch=='+':
    print("Addition is:",add(a,b))
elif ch=='-':
    print("Subtraction is:",sub(a,b))
elif ch=='*':
    print("Multiplication is:",mul(a,b))
elif ch=='/':
    print("Division is:",div(a,b))
else:
    print("Invalid operation")
