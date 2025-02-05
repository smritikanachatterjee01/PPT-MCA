# 10. Nested Dictionary & Accessing Elements
students = {
    "John": {"age": 20, "grades": [85, 90, 92]},
    "Emma": {"age": 22, "grades": [88, 79, 95]}
}

# Print John's age
print("John's age:", students["John"]["age"])

# Print Emma's highest grade
print("Emma's highest grade:", max(students["Emma"]["grades"]))