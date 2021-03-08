import random
names = ["Shahram", "Sara", "Angela", "Bahar", "Caroline"]

students_scores = {student: random.randint(1, 100) for student in names}
passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
print(students_scores)
print(passed_students)
