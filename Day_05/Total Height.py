# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# total_height = sum(student_heights)
# number_of_students = len(student_heights)
# average_height = round(total_height / number_of_students)
# print(average_height)
total_height = 0
for height in student_heights:
  total_height += height
print("Total heights Students:",total_height)

# number_of_student = len(student_heights)
# average_height = round(total_height / number_of_student)
# print(average_height)
number_of_student = 0
for student in student_heights:
  number_of_student += 1
print("Number Of Students",number_of_student)