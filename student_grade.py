name = input("Enter student name: ")

maths = int(input("Enter Maths marks: "))
chemistry = int(input("Enter Chemistry marks: "))
physics = int(input("Enter Physics marks: "))
english = int(input("Enter English marks: "))
python_marks = int(input("Enter Python marks: "))

marks = [maths, chemistry, physics, english, python_marks]

if any(mark < 0 or mark > 100 for mark in marks):
    print("Invalid marks! Enter marks between 0 and 100.")
else:
    total = sum(marks)
    percentage = total / 5

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

    print("\n--- Student Result ---")
    print("Student Name:", name)
    print("Total:", total, "/ 500")
    print("Percentage:", percentage, "%")
    print("Grade:", grade)

    if all(mark >= 40 for mark in marks):
        print("Result: PASS")
    else:
        print("Result: FAIL")
