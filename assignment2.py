def find_max(numbers):
    if not numbers:
        return None  # Returns None if the list is empty

result = find_max([])
print(result + 5)  # Runtime error: TypeError (NoneType + int)
