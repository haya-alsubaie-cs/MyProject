# smart_calculator_v2.py

from datetime import datetime

# History list to store previous calculations
calculation_history = []

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None  # Division by zero handled separately
    return a / b

def compute_expression(a, b, c):
    """
    Computes a + (b * c) and returns result with intermediate steps.
    """
    product = multiply(b, c)
    result = add(a, product)
    # Save to history
    calculation_history.append({
        "expression": f"{a} + ({b} * {c})",
        "result": result,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    return product, result

def get_number(prompt):
    """
    Validates user input and returns an integer.
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("⚠️ Invalid input! Please enter a number.")

def show_history():
    if not calculation_history:
        print("No previous calculations yet.")
        return
    print("\n=== Calculation History ===")
    for record in calculation_history:
        print(f"{record['timestamp']}: {record['expression']} = {record['result']}")
    print("===========================\n")

def main():
    print("💡 Welcome to Your Smart Calculator 💡\n")
    
    while True:
        a = get_number("Enter first number (a): ")
        b = get_number("Enter second number (b): ")
        c = get_number("Enter third number (c): ")

        product, result = compute_expression(a, b, c)
        print(f"\nStep 1: Multiply {b} * {c} = {product}")
        print(f"Step 2: Add {a} + {product} = {result}")
        print(f"✅ Result: {result}\n")

        show_history()

        choice = input("Do you want to calculate again? (y/n): ").strip().lower()
        if choice != 'y':
            print("👋 Goodbye! Thanks for using Smart Calculator.")
            break

if __name__ == "__main__":
    main()
