def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
print(any_lowercase4("HELLO"))  # Returns False (Correct)
print(any_lowercase4("Hello"))  # Returns True (Correct)
print(any_lowercase4("hello"))  # Returns True (Correct)
