import os
import sys
from urllib.parse import urlencode

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def main():
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
    }

    print("Welcome to the HYDRA Calculator!")
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    try:
        result = operations[operator](num1, num2)
        print(f"Result: {result}")
    except KeyError:
        print("Invalid operator. Please use +, -, *, or /.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()