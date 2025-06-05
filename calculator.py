#!/usr/bin/env python3
"""Simple command line calculator.

Supports addition, subtraction, multiplication, and division.
Run the script and follow the prompts or import the functions elsewhere.
"""


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y


def main():
    operations = {
        "1": (add, "Add"),
        "2": (subtract, "Subtract"),
        "3": (multiply, "Multiply"),
        "4": (divide, "Divide"),
    }
    while True:
        print("Select operation:")
        for key, (_, name) in operations.items():
            print(f"{key}. {name}")
        choice = input("Enter choice (or 'q' to quit): ")
        if choice.lower() == 'q':
            break
        if choice not in operations:
            print("Invalid choice")
            continue
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = operations[choice][0](num1, num2)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)
        print()


if __name__ == "__main__":
    main()
