def modify_list(lst):
    """Appends an item to the list passed as an argument"""
    lst.append("modified")

# Create a list and pass it to the function
my_list = [1, 2, 3]
modify_list(my_list)

print(my_list)  # Output: [1, 2, 3, "modified"]
