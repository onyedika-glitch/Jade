# Function to convert a sentence into a word list and reverse it
def reverse_wordlist(sentence):
    words = sentence.split()  # Splitting sentence into words using space as a delimiter
    reversed_words = words[::-1]  # Reversing the word list
    return reversed_words  # Returning the reversed list

# Example usage
sentence = "Hello world this is Python"
result = reverse_wordlist(sentence)

# Output results
print("Original Sentence:", sentence)
print("Reversed Word List:", result)
