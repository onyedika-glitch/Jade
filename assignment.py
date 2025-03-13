def divide(a, b):
    # Precondition: b should not be zero
    if b == 0:
        return "Error: Cannot divide by zero"
    
    return a / b

print(divide(10, 0))  # Output: Error: Cannot divide by zero
