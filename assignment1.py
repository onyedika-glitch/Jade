def calculate_discount(price):
    # Incorrect formula (logic error)
    return price + 0.1 * price  # Should be price - 0.1 * price

print(calculate_discount(100))  # Wrong output: 110 (Expected: 90)
