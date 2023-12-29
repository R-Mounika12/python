import sys

## command line arguments are read from 'sys' module

def add(num1, num2):
    return num1+num2

def sub(num1, num2):
    return num1-num2

def mul(num1, num2):
    return num1*num2

def div(num1, num2):
    return num1/num2

num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
operation = sys.argv[3]

addition = add(num1, num2)
subtraction = sub(num1, num2)
multiplication = mul(num1, num2)
division = div(num1, num2)

if operation == "add":
    print("add : ", add(num1, num2))
elif operation == "sub":
    print("sub : ", sub(num1, num2))
elif operation == "mul":
    print("mul : ", mul(num1, num2))
else :
    print("div : ", div(num1, num2))
