name = input("Enter student name: ")

maths = int(input("Enter Maths marks: "))
chemistry = int(input("Enter Chemistry marks: "))
physics = int(input("Enter Physics marks: "))
english = int(input("Enter English marks: "))
python_marks = int(input("Enter Python marks: "))

total = maths + chemistry + physics + english + python_marks
percentage = total / 5

print("Student Name:", name)
print("Total:", total)
print("Percentage:", percentage, "%")

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)
