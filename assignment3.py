def divide(a, b):
    """Returns the result of a divided by b"""
    # Precondition: 'b' should not be zero
    if b == 0:
        return "Error: Cannot divide by zero"
    
    result = a / b

    # Postcondition: The result should be a valid quotient
    return result

print(divide(10, 2))  # Output: 5.0
print(divide(5, 0))   # Output: Error: Cannot divide by zero
