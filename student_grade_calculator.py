import json
import os

# Global configuration constants
DATA_FILE = "student_records.json"

def load_records():
    """Reads saved student evaluations from persistent file arrays."""
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        print("Notice: Error processing records database. Initializing blank database framework.")
        return {}

def save_records(records):
    """Saves system structural arrays out to local persistent directories."""
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(records, file, indent=4)
    except IOError:
        print("Error: Could not save persistent academic data updates.")

def calculate_grade_metrics(marks, passing_criteria=35.0):
    """Core mathematical engine logic to extract percentages and operational outcomes."""
    if not marks:
        return 0.0, 0.0, 0.0, "F", "FAIL"
        
    total = sum(marks.values())
    count = len(marks)
    max_possible = count * 100.0
    average = total / count
    percentage = (total / max_possible) * 100.0

    # Business evaluation logic rules mapping metrics out to targeted structural tiers
    if any(m < passing_criteria for m in marks.values()):
        grade = "F"
        result = "FAIL"
    elif percentage >= 90.0:
        grade = "A Plus"
        result = "PASS"
    elif percentage >= 80.0:
        grade = "A"
        result = "PASS"
    elif percentage >= 70.0:
        grade = "B"
        result = "PASS"
    elif percentage >= 60.0:
        grade = "C"
        result = "PASS"
    elif percentage >= passing_criteria:
        grade = "D"
        result = "PASS"
    else:
        grade = "F"
        result = "FAIL"
        
    return total, average, percentage, grade, result

def add_student_profile(records):
    """Processes iterative validation inputs to insert profiles into standard workspaces."""
    name = input("Enter student name: ").strip()
    if not name:
        print("Error: Student designation profile cannot be blank.")
        return

    # Dynamic modular modification configuration parameter
    print("Default subjects: Maths, Chemistry, Physics, Python, English")
    use_custom = input("Configure custom subject listings for this profile? (yes/no): ").strip().lower()
    
    if use_custom == "yes":
        subjects_input = input("Enter subjects separated by spaces: ").strip()
        subjects = [s.strip().title() for s in subjects_input.split() if s.strip()]
        if not subjects:
            print("Notice: Input sequence failed to capture labels. Resets down to default values.")
            subjects = ["Maths", "Chemistry", "Physics", "Python", "English"]
    else:
        subjects = ["Maths", "Chemistry", "Physics", "Python", "English"]

    try:
        passing_input = input("Set customized subject pass limit threshold (Default 35): ").strip()
        passing_criteria = float(passing_input) if passing_input else 35.0
        if not (0.0 <= passing_criteria <= 100.0):
            print("Notice: Boundary constraint violation detected. Limit normalized down to 35.")
            passing_criteria = 35.0
    except ValueError:
        print("Notice: Non-numeric parsing values flagged. Limit normalized down to 35.")
        passing_criteria = 35.0

    marks = {}
    for sub in subjects:
        while True:
            try:
                mark_input = input(f"Enter {sub} marks from zero to 100: ").strip()
                mark = float(mark_input)
                if 0.0 <= mark <= 100.0:
                    marks[sub] = mark
                    break
                else:
                    print("Error: Boundary limitation failure. Numeric scale parameters stand between zero and 100.")
            except ValueError:
                print("Error: Numeric conversion layer blocked. Provide functional digits.")

    total, average, percentage, grade, result = calculate_grade_metrics(marks, passing_criteria)

    records[name] = {
        "marks": marks,
        "passing_criteria": passing_criteria,
        "total": round(total, 2),
        "average": round(average, 2),
        "percentage": round(percentage, 2),
        "grade": grade,
        "result": result
    }
    
    save_records(records)
    print(f"Success: Academic card profile updated successfully for {name}.")

def view_individual_report(records):
    """Locates explicit items to output historical operational analytics cards."""
    if not records:
        print("No student evaluation logs discovered within active datasets.")
        return

    name = input("Enter student profile query label to extract: ").strip()
    if name not in records:
        print("Error: Targets matching that profile identity key are missing.")
        return

    profile = records[name]
    print("\n--- STUDENT REPORT CARD ---")
    print(f"Student Identity Label: {name}")
    print("Subject Marks Breakdown:")
    for subject, mark in profile["marks"].items():
        print(f"  Subject: {subject} | Score: {mark:.2f}")
    
    print(f"Total Cumulative Marks: {profile['total']:.2f} / {len(profile['marks']) * 100}")
    print(f"Calculated Score Average: {profile['average']:.2f}")
    print(f"Calculated Outright Percentage: {profile['percentage']:.2f}")
    print(f"Allocated Tier Grade: {profile['grade']}")
    print(f"Final Academic Determination Status: {profile['result']}")
    print(f"Minimum Subject Passing Boundary Requirement: {profile['passing_criteria']:.2f}")

def display_class_aggregates(records):
    """Calculates macro metrics comparing metrics across all recorded entities."""
    if not records:
        print("No records structural values available to extract comparative reports.")
        return

    total_students = len(records)
    all_percentages = [p["percentage"] for p in records.values()]
    class_average_pct = sum(all_percentages) / total_students
    
    highest_profile = max(records.items(), key=lambda item: item[1]["percentage"])
    lowest_profile = min(records.items(), key=lambda item: item[1]["percentage"])

    print("\n--- CLASS ROOM PERFORMANCE SUMMARY AND AGGREGATES ---")
    print(f"Total Number of Tracked Academic Profiles: {total_students}")
    print(f"Calculated Total Group Average Percentage: {class_average_pct:.2f}")
    print(f"Leading Tracked Performer: {highest_profile[0]} with Percentage: {highest_profile[1]['percentage']:.2f}")
    print(f"Trailing Tracked Performer: {lowest_profile[0]} with Percentage: {lowest_profile[1]['percentage']:.2f}")

def execute_automated_diagnostic_tests():
    """Runs functional operations validation sequences across logic code pathways."""
    print("\n--- RUNNING DIAGNOSTIC SYSTEM INTERFACE CHECKS ---")
    
    # Check Case A: Clean execution loop pass
    test_marks_pass = {"Maths": 95.0, "Chemistry": 90.0, "Physics": 85.0}
    t, a, p, g, r = calculate_grade_metrics(test_marks_pass, passing_criteria=35.0)
    
    assert t == 270.0, f"Error: Expecting 270, got {t}"
    assert a == 90.0, f"Error: Expecting 90, got {a}"
    assert p == 90.0, f"Error: Expecting 90, got {p}"
    assert g == "A Plus", f"Error: Expecting A Plus, got {g}"
    assert r == "PASS", f"Error: Expecting PASS, got {r}"
    print("Diagnostic Sub-Check 1 Passed: Performance evaluation checks confirm absolute calibration matches standard models.")

    # Check Case B: Individual component failure path check
    test_marks_fail = {"Maths": 95.0, "Chemistry": 30.0, "Physics": 85.0}
    _, _, _, g_f, r_f = calculate_grade_metrics(test_marks_fail, passing_criteria=35.0)
    
    assert g_f == "F", f"Error: Expecting F, got {g_f}"
    assert r_f == "FAIL", f"Error: Expecting FAIL, got {r_f}"
    print("Diagnostic Sub-Check 2 Passed: Single subject target shortfalls trigger safe termination flags.")
    
    print("All internal functional code units passed verification testing operations cleanly.")

def main():
    """Initializes primary engine execution paths."""
    database_context = load_records()

    while True:
        print("\n===== ACADEMIC TRACKING AND MEASUREMENT CONSOLE V5 =====")
        print("1. Record New Student Marks Profile")
        print("2. Extract Explicit Student Report Card")
        print("3. Review Cross-Class Comparative Metric Aggregates")
        print("4. Trigger Automated Engine Code Diagnostics Test Suite")
        print("5. Terminate Evaluation Engine Session")

        choice = input("Select tracking node interface selection parameter (1-5): ").strip()

        if choice == "1":
            add_student_profile(database_context)
        elif choice == "2":
            view_individual_report(database_context)
        elif choice == "3":
            display_class_aggregates(database_context)
        elif choice == "4":
            execute_automated_diagnostic_tests()
        elif choice == "5":
            print("System down cycle sequence initialized. Session tracking closed safely.")
            break
        else:
            print("Error: Input parameter selection node falls outside designated framework bounds.")

if __name__ == "__main__":
    main()
