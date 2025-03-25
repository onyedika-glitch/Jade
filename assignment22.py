try:
    # Attempt to open a file that does not exist
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError as e:
    # Handle the file not found error
    print(f"Error: {e}")
    print("The file you are trying to access does not exist. Please check the file name or path.")
