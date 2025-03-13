def calculate_simple_interest(p, r, t):
    return 0  # Placeholder for now
import math

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)
print(calculate_hypotenuse(3, 4))  # Expected output: 5.0
print(calculate_hypotenuse(5, 12)) # Expected output: 13.0
print(calculate_hypotenuse(8, 15)) # Expected output: 17.0
def calculate_hypotenuse(a, b):
    if a <= 0 or b <= 0:
        return "Error: Side lengths must be positive numbers."
    
    return round(math.sqrt(a**2 + b**2), 2)
print(calculate_hypotenuse(-3, 4))  # Expected output: Error message
print(calculate_hypotenuse(7, 24))  # Expected output: 25.0
print(calculate_hypotenuse(6, 8))   # Expected output: 10.0