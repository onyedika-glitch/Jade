names = ("Alice", "Bob", "Charlie")
scores = (85, 90, 78)

# Using zip to combine names and scores into tuples
for name, score in zip(names, scores):
    print(f"{name} scored {score}")
