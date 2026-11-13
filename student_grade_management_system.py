"""
Student Grade Management System
A simple command-line application for recording student marks,
calculating averages, assigning letter grades, and displaying results.

Grade scale:
A = 90-100, B = 80-89, C = 70-79, D = 60-69, F = below 60
"""

def get_non_empty(prompt):
    """Ask until the user enters a non-empty value."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def get_mark(subject):
    """Read and validate a mark from 0 to 100."""
    while True:
        raw = input(f"Enter mark for {subject} (0-100): ").strip()
        try:
            mark = float(raw)
            if 0 <= mark <= 100:
                return mark
            print("Invalid mark. Enter a value between 0 and 100.")
        except ValueError:
            print("Invalid input. Enter a number, for example 78 or 85.5.")


def calculate_average(marks):
    """Return the arithmetic mean of a list of marks."""
    return sum(marks) / len(marks)


def calculate_grade(average):
    """Convert an average mark to a letter grade."""
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


def add_student(students, subjects):
    """Collect one student's details and marks, then store the record."""
    print("\n--- Add Student ---")
    student_id = get_non_empty("Student ID: ")

    if any(student["id"].lower() == student_id.lower() for student in students):
        print("A student with that ID already exists.")
        return

    name = get_non_empty("Student name: ")
    marks = [get_mark(subject) for subject in subjects]
    average = calculate_average(marks)

    students.append({
        "id": student_id,
        "name": name,
        "marks": marks,
        "average": average,
        "grade": calculate_grade(average)
    })
    print(f"Student {name} added successfully.")


def display_student(student, subjects):
    """Print a formatted report for one student."""
    print("\n" + "=" * 48)
    print(f"Student ID : {student['id']}")
    print(f"Name       : {student['name']}")
    for subject, mark in zip(subjects, student["marks"]):
        print(f"{subject:<12}: {mark:>6.2f}")
    print("-" * 48)
    print(f"Average    : {student['average']:.2f}")
    print(f"Letter grade: {student['grade']}")
    print("=" * 48)


def display_all_students(students, subjects):
    """Display all saved student results."""
    if not students:
        print("\nNo student records have been entered yet.")
        return

    print("\n--- All Student Results ---")
    for student in students:
        display_student(student, subjects)


def search_student(students, subjects):
    """Find and display a student using their ID."""
    student_id = get_non_empty("Enter the student ID to search: ")
    for student in students:
        if student["id"].lower() == student_id.lower():
            display_student(student, subjects)
            return
    print("No student was found with that ID.")


def show_grade_scale():
    """Explain the grade boundaries."""
    print("\n--- Grade Scale ---")
    print("A: 90-100")
    print("B: 80-89.99")
    print("C: 70-79.99")
    print("D: 60-69.99")
    print("F: Below 60")


def main():
    print("STUDENT GRADE MANAGEMENT SYSTEM")
    print("--------------------------------")
    print("This project uses five subjects. You can change them in the code.")
    subjects = ["English", "Mathematics", "Biology", "Chemistry", "Physics"]
    students = []

    while True:
        print("\nMAIN MENU")
        print("1. Add student and marks")
        print("2. Display all student results")
        print("3. Search for a student")
        print("4. Show grade scale")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_student(students, subjects)
        elif choice == "2":
            display_all_students(students, subjects)
        elif choice == "3":
            if students:
                search_student(students, subjects)
            else:
                print("There are no student records to search.")
        elif choice == "4":
            show_grade_scale()
        elif choice == "5":
            print("Thank you for using the Student Grade Management System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
