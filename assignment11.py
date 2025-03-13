def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
print(any_lowercase5("Hello"))  # Returns False (Incorrect)
print(any_lowercase5("hello"))  # Returns True (Correct)
print(any_lowercase5("HELLO"))  # Returns False (Correct)
