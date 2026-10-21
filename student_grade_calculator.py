
import json
import os

DATA_FILE = "student_records.json"
DEFAULT_SUBJECTS = ["Maths", "Chemistry", "Physics", "Python", "English"]


def load_records():
    if not os.path.exists(DATA_FILE):
        return {}

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Error reading database. Starting with empty records.")
        return {}


def save_records(records):
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(records, file, indent=4)
    except OSError:
        print("Error saving student records.")


def calculate_grade_metrics(marks, passing_criteria=35.0):
    if not marks:
        return 0, 0, 0, "F", "FAIL"

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


def add_student(records):
    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    print("Default subjects:", ", ".join(DEFAULT_SUBJECTS))
    choice = input("Use custom subjects? (yes/no): ").strip().lower()

    if choice == "yes":
        subjects = [
            s.strip().title()
            for s in input("Enter subjects separated by commas: ").split(",")
            if s.strip()
        ]
        if not subjects:
            subjects = DEFAULT_SUBJECTS.copy()
    else:
        subjects = DEFAULT_SUBJECTS.copy()

    try:
        passing = input("Passing marks (default 35): ").strip()
        passing = float(passing) if passing else 35.0

        if not 0 <= passing <= 100:
            raise ValueError
    except ValueError:
        print("Invalid passing marks. Using 35.")
        passing = 35.0

    marks = {}

    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter {subject} marks (0-100): "))

                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break

                print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    total, avg, pct, grade, result = calculate_grade_metrics(
        marks, passing
    )

    records[name] = {
        "marks": marks,
        "passing_criteria": passing,
        "total": round(total, 2),
        "average": round(avg, 2),
        "percentage": round(pct, 2),
        "grade": grade,
        "result": result
    }

    save_records(records)
    print(f"Student record saved successfully for {name}!")


def view_report(records):
    name = input("Enter student name: ").strip()

    if name not in records:
        print("Student not found.")
        return

    student = records[name]

    print("\n===== STUDENT REPORT CARD =====")
    print("Name:", name)

    for subject, mark in student["marks"].items():
        print(f"{subject}: {mark:.2f}/100")

    print(f"Total: {student['total']:.2f}/"
          f"{len(student['marks']) * 100}")
    print(f"Average: {student['average']:.2f}")
    print(f"Percentage: {student['percentage']:.2f}%")
    print("Grade:", student["grade"])
    print("Result:", student["result"])
    print("Passing marks:", student["passing_criteria"])


def class_summary(records):
    if not records:
        print("No student records available.")
        return

    percentages = {
        name: student["percentage"]
        for name, student in records.items()
    }

    average = sum(percentages.values()) / len(percentages)
    highest = max(percentages, key=percentages.get)
    lowest = min(percentages, key=percentages.get)

    print("\n===== CLASS PERFORMANCE SUMMARY =====")
    print("Total students:", len(records))
    print(f"Class average: {average:.2f}%")
    print(f"Highest scorer: {highest} "
          f"({percentages[highest]:.2f}%)")
    print(f"Lowest scorer: {lowest} "
          f"({percentages[lowest]:.2f}%)")


def run_tests():
    print("\n===== RUNNING DIAGNOSTIC TESTS =====")

    marks = {"Maths": 95, "Chemistry": 90, "Physics": 85}
    total, avg, pct, grade, result = calculate_grade_metrics(marks)

    assert total == 270
    assert avg == 90
    assert pct == 90
    assert grade == "A Plus"
    assert result == "PASS"

    failed_marks = {"Maths": 95, "Chemistry": 30, "Physics": 85}
    _, _, _, grade, result = calculate_grade_metrics(failed_marks)

    assert grade == "F"
    assert result == "FAIL"

    print("Test 1 passed: Grade calculation.")
    print("Test 2 passed: Failed subject detection.")
    print("All diagnostic tests passed!")


def main():
    records = load_records()

    while True:
        print("\n===== STUDENT MARKS MANAGEMENT SYSTEM =====")
        print("1. Add Student Marks")
        print("2. View Student Report")
        print("3. Class Performance Summary")
        print("4. Run Diagnostic Tests")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_student(records)
        elif choice == "2":
            view_report(records)
        elif choice == "3":
            class_summary(records)
        elif choice == "4":
            run_tests()
        elif choice == "5":
            print("Program closed successfully. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()
