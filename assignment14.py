a = [10, 20, 30]
b = a  # Both 'a' and 'b' refer to the same list
b.append(40)

print(a)  # Output: [10, 20, 30, 40], because 'a' and 'b' reference the same object
