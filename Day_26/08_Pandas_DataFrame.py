import  pandas

student_dict = {
    "student": ["Shahram", "Sara", "Angela", "Bahar", "Caroline"],
    "score": [99, 56, 78, 80, 65]
    }

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Shahram":
        print(row.score)
