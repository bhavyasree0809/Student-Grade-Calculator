name = input("Enter student name: ")

maths = int(input("Enter Maths marks: "))
chemistry = int(input("Enter Chemistry marks: "))
physics = int(input("Enter Physics marks: "))
english = int(input("Enter English marks: "))
python_marks = int(input("Enter Python marks: "))

marks = {
    "Maths": maths,
    "Chemistry": chemistry,
    "Physics": physics,
    "English": english,
    "Python": python_marks
}

if any(mark < 0 or mark > 100 for mark in marks.values()):
    print("Invalid marks! Enter marks between 0 and 100.")

else:
    total = sum(marks.values())
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

    print("\n--- Subject Results ---")

    for subject, mark in marks.items():
        if mark >= 40:
            print(subject + ":", "PASS")
        else:
            print(subject + ":", "FAIL")

    if all(mark >= 40 for mark in marks.values()):
        print("\nOverall Result: PASS")
    else:
        print("\nOverall Result: FAIL")
