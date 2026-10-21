
def calculate_grade_metrics(marks, passing_criteria=35):
    total = sum(marks.values())
    average = total / len(marks)
    percentage = average

    if any(mark < passing_criteria for mark in marks.values()):
        grade, result = "F", "FAIL"
    elif percentage >= 90:
        grade, result = "A Plus", "PASS"
    elif percentage >= 80:
        grade, result = "A", "PASS"
    elif percentage >= 70:
        grade, result = "B", "PASS"
    elif percentage >= 60:
        grade, result = "C", "PASS"
    else:
        grade, result = "D", "PASS"

    return total, average, percentage, grade, result


def main():
    students = {}

    while True:
        print("\n===== STUDENT MARKS MANAGEMENT =====")
        print("1. Add Student")
        print("2. View Student Report")
        print("3. Class Summary")
        print("4. Run Tests")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            subjects = ["Maths", "Chemistry", "Physics", "Python", "English"]
            marks = {}

            for subject in subjects:
                while True:
                    try:
                        mark = float(input(f"Enter {subject} marks: "))
                        if 0 <= mark <= 100:
                            marks[subject] = mark
                            break
                        print("Enter marks between 0 and 100.")
                    except ValueError:
                        print("Enter a valid number.")

            total, avg, pct, grade, result = calculate_grade_metrics(marks)

            students[name] = {
                "marks": marks,
                "total": total,
                "average": avg,
                "percentage": pct,
                "grade": grade,
                "result": result
            }

            print("Student added successfully!")

        elif choice == "2":
            name = input("Enter student name: ")

            if name in students:
                s = students[name]
                print("\n===== REPORT CARD =====")
                print("Name:", name)
                print("Marks:", s["marks"])
                print("Total:", s["total"], "/ 500")
                print("Average:", s["average"])
                print("Percentage:", s["percentage"], "%")
                print("Grade:", s["grade"])
                print("Result:", s["result"])
            else:
                print("Student not found.")

        elif choice == "3":
            if students:
                percentages = [
                    s["percentage"] for s in students.values()
                ]
                print("Total students:", len(students))
                print("Class average:",
                      round(sum(percentages) / len(percentages), 2), "%")
                print("Highest percentage:", max(percentages), "%")
                print("Lowest percentage:", min(percentages), "%")
            else:
                print("No student records available.")

        elif choice == "4":
            marks = {"Maths": 95, "Chemistry": 90, "Physics": 85}
            total, avg, pct, grade, result = calculate_grade_metrics(marks)

            assert total == 270
            assert avg == 90
            assert grade == "A Plus"
            assert result == "PASS"

            print("Grade calculation test passed!")

            marks = {"Maths": 95, "Chemistry": 30, "Physics": 85}
            _, _, _, grade, result = calculate_grade_metrics(marks)

            assert grade == "F"
            assert result == "FAIL"
            print("Fail detection test passed!")
            print("All tests passed successfully!")

        elif choice == "5":
            print("Program closed successfully!")
            break

        else:
            print("Invalid choice. Enter 1 to 5.")


if __name__ == "__main__":
    main()
