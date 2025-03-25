subjects = ("Math", "Science", "History")

# Using enumerate to get index and value
for index, subject in enumerate(subjects, start=1):
    print(f"Subject {index}: {subject}")
