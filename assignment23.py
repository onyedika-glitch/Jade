import logging

logging.basicConfig(filename="app.log", level=logging.ERROR)
try:
    with open("data.txt", "r") as file:
        data = file.read()
except FileNotFoundError as e:
    logging.error(f"File not found: {e}")
try:
    with open("protected_file.txt", "w") as file:
        file.write("Test")
except PermissionError as e:
    print("You do not have permission to write to this file.")
