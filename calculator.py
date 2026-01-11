"""
Simple Calculator Module

This module provides basic arithmetic operations including
addition, subtraction, multiplication, division, and power operations.
"""


class Calculator:
    """A simple calculator class with basic arithmetic operations."""
    
    def add(self, a, b):
        """Add two numbers and return the result."""
        return b + a
    
    def subtract(self, a, b):
        """Subtract second number from first and return the result."""
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers and return the result."""
        return a * b
        
    def divide(self, a, b):
        """Divide first number by second and return the result."""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b

    



def main():
    """Main function to demonstrate calculator usage."""
    calc = Calculator()
    
    print("Simple Calculator Demo")
    print("=" * 25)
    
    # Demo calculations
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")

if __name__ == "__main__":
    main()
