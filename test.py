"""Module for managing and reporting student grades."""

class Student:
    """Represents a student with his grades and academic status."""
    def __init__(self, student_id: str, name: str):
        if not str(student_id).strip():
            raise ValueError("The student ID cannot be empty.")
        if not str(name).strip():
            raise ValueError("The student's name cannot be empty.")
        self.student_id = str(student_id).strip()
        self.name = str(name).strip()
        self.grades = []
        self.letter = "N/A"

    def add_grade(self, grade):
        """Add a numerical note if it is in the allowed range (0.0 to 100.0)."""
        if isinstance(grade, bool) or not isinstance(grade, (int, float)):
            print(f"Error: The note '{grade}' is not numerical.")
            return False
        grade_val = float(grade)
        if 0.0 <= grade_val <= 100.0:
            self.grades.append(grade_val)
            return True
        print(f"Error: The note {grade_val} is outside the range 0.0 to 100.0.")
        return False

    def calc_average(self):
        """Calculate the average of the student's grades."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self):
        """Assigns and returns the corresponding letter based on the average."""
        avg = self.calc_average()
        if avg >= 90.0:
            return "A"
        if avg >= 80.0:
            return "B"
        if avg >= 70.0:
            return "C"
        if avg >= 60.0:
            return "D"
        return "F"

    def is_passed(self):
        """Returns 'Passed' if the average is greater than or equal to 60, but 'Failed'."""
        return "Passed" if self.calc_average() >= 60.0 else "Failed"

    def is_honor_roll(self):
        """Returns True if the average is greater than or equal to 90."""
        return self.calc_average() >= 90.0

    def delete_grade_by_index(self, index: int):
        """Deletes a note given its position in the list."""
        if isinstance(index, int) and 0 <= index < len(self.grades):
            removed = self.grades.pop(index)
            print(f"Note {removed} removed in index {index}.")
            return True
        print(f"Error: The index {index} is invalid or out of range.")
        return False

    def delete_grade_by_value(self, value: float):
        """Eliminates the first occurrence of a specific note."""
        try:
            val_float = float(value)
            if val_float in self.grades:
                self.grades.remove(val_float)
                print(f"Note {val_float} successfully removed.")
                return True
        except (ValueError, TypeError):
            pass
        print(f"Error: The note {value} does not exist in the record.")
        return False

    def report(self):  # broken format
        """Displays the student's formatted academic summary on the screen."""
        print("-" * 40)
        print("STUDENT REPORT")
        print("-" * 40)
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Number of notes: {len(self.grades)}")
        print(f"Average: {self.calc_average():.2f}")
        print(f"Letter rating: {self.get_letter_grade()}")
        print(f"Status: {self.is_passed()}")
        print(f"Box of Honor: {self.is_honor_roll()}")
        print("-" * 40)

def main():
    """Demonstrates complete operation without uncaptured exceptions."""
    print("=== PROOF OF CREATION WITH INVALID DATA ===")
    try:
        Student("", "John Doe")
    except ValueError as err:
        print(f"Captured correctly: {err}")

    print("\n=== STUDENT REGISTRATION AND OPERATIONS ===")
    student = Student("ST-101", "John Doe")

    # Add valid and invalid notes
    student.add_grade(95.0)
    student.add_grade(85.5)
    student.add_grade(105.0) # Out of rank
    student.add_grade("Fifty") # Non-numeric type
    student.add_grade(92.0)

    # Show initial report
    student.report()

    # Elimination by index and by value
    print("\n=== NOTE DELETION TESTS ===")
    student.delete_grade_by_index(1) # Removes 85.5
    student.delete_grade_by_index(10) # Invalid index
    student.delete_grade_by_value(95.0) # Removes 95.0
    student.delete_grade_by_value(40.0) # Nonexistent value

    # Show final report after editions
    print("\n=== FINAL REPORT ===")
    student.report()

if __name__ == "__main__":
    main()
