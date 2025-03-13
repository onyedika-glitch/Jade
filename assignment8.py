def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
print(any_lowercase2("HELLO"))  # Returns 'True' (Incorrect)
