# Program to perform operations on a name entered by the user

# Accept user's name as input
name = input("Enter your name: ")

# Accept the number of characters to display from the left
n = int(input("Enter the number of characters to display from the left: "))

# Function to display n characters from the left
def display_n_chars(name, n):
    return name[:n]  # Slicing to get the first n characters

# Function to count the number of vowels in the name
def count_vowels(name):
    vowels = "aeiouAEIOU"  # Define vowels (both uppercase and lowercase)
    count = sum(1 for char in name if char in vowels)  # Count vowels in the name
    return count

# Function to reverse the name
def reverse_name(name):
    return name[::-1]  # String slicing to reverse the name

# Perform operations
first_n_chars = display_n_chars(name, n)
vowel_count = count_vowels(name)
reversed_name = reverse_name(name)

# Display results
print("\nResults:")
print(f"First {n} characters: {first_n_chars}")
print(f"Number of vowels: {vowel_count}")
print(f"Reversed name: {reversed_name}")
