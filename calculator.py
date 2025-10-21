#!/usr/bin/env python3
"""
Simple Calculator Script
Performs basic arithmetic operations: addition, subtraction, multiplication, and division.
"""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def main():
    """Main function to run the calculator."""
    print("Simple Calculator")
    print("=" * 40)
    print("Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("=" * 40)

    try:
        # Get operation choice
        choice = input("\nSelect operation (1-4): ")

        # Get numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Perform calculation
        if choice == '1':
            result = add(num1, num2)
            print(f"\n{num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"\n{num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"\n{num1} * {num2} = {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"\n{num1} / {num2} = {result}")
        else:
            print("\nInvalid choice! Please select 1-4.")

    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
