# 9. Finding Maximum and Minimum Values in a Dictionary
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95}

# Find the student with the highest score
highest_score = max(scores.values())
highest_student = [student for student, score in scores.items() if score == highest_score][0]

# Find the student with the lowest score
lowest_score = min(scores.values())
lowest_student = [student for student, score in scores.items() if score == lowest_score][0]

print(f"Student with the highest score: {highest_student} ({highest_score})")
print(f"Student with the lowest score: {lowest_student} ({lowest_score})")


