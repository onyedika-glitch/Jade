def invert_dictionary(student_courses):
    inverted_dict = {}

    for student, courses in student_courses.items():
        for course in courses:
            if course not in inverted_dict:
                inverted_dict[course] = []
            inverted_dict[course].append(student)

    return inverted_dict

# Sample input
student_courses = {
    'Stud1': ['CS1101', 'CS2402', 'CS2001'],
    'Stud2': ['CS2402', 'CS2001', 'CS1102']
}

# Get inverted dictionary
inverted_dict = invert_dictionary(student_courses)

# Print output
print(inverted_dict)
