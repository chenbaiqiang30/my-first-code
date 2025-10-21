#!/usr/bin/env python3
"""Test script for the calculator functions."""

from calculator import add, subtract, multiply, divide

def test_operations():
    """Test all calculator operations."""
    print("Testing Calculator Operations")
    print("=" * 40)

    # Test addition
    result = add(5, 3)
    print(f"Addition: 5 + 3 = {result}")
    assert result == 8, "Addition failed!"

    # Test subtraction
    result = subtract(10, 4)
    print(f"Subtraction: 10 - 4 = {result}")
    assert result == 6, "Subtraction failed!"

    # Test multiplication
    result = multiply(6, 7)
    print(f"Multiplication: 6 * 7 = {result}")
    assert result == 42, "Multiplication failed!"

    # Test division
    result = divide(20, 4)
    print(f"Division: 20 / 4 = {result}")
    assert result == 5, "Division failed!"

    # Test division by zero
    print("\nTesting division by zero...")
    try:
        divide(10, 0)
        print("ERROR: Should have raised ValueError!")
    except ValueError as e:
        print(f"Correctly raised error: {e}")

    print("\n" + "=" * 40)
    print("All tests passed!")

if __name__ == "__main__":
    test_operations()
