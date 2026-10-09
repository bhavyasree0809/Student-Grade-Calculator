
# Student Grade Calculator - Version 4

print("===== STUDENT GRADE CALCULATOR V4 =====")

name = input("Enter student name: ")

subjects = ["Maths", "Chemistry", "Physics", "Python", "English"]
marks = []

for subject in subjects:
    while True:
        try:
            mark = float(input(f"Enter {subject} marks (0-100): "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

total = sum(marks)
average = total / len(subjects)
percentage = (total / (len(subjects) * 100)) * 100

if any(mark < 35 for mark in marks):
    grade = "F"
    result = "FAIL"
elif percentage >= 90:
    grade = "A+"
    result = "PASS"
elif percentage >= 80:
    grade = "A"
    result = "PASS"
elif percentage >= 70:
    grade = "B"
    result = "PASS"
elif percentage >= 60:
    grade = "C"
    result = "PASS"
elif percentage >= 35:
    grade = "D"
    result = "PASS"
else:
    grade = "F"
    result = "FAIL"

print("\n===== STUDENT REPORT CARD =====")
print("Student Name:", name)

for i in range(len(subjects)):
    print(subjects[i], ":", marks[i])

print("Total Marks:", total, "/ 500")
print("Average:", round(average, 2))
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
print("Final Result:", result)

print("===== THANK YOU =====")
