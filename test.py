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
        self.honor = "?"
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

    def delete_grade(self, index):
        """Delete a note by its index if it is valid."""
        if 0 <= index < len(self.grades):
            del self.grades[index]

    def report(self):  # broken format
        """Shows the student's academic summary on the screen."""
        print(f"ID: {self.student_id}")
        print(f"Name is: {self.name}")
        print(f"Grades Count: {len(self.grades)}")
        print(f"Average: {self.calc_average():.2f}")
        print(f"Final Grade = {self.letter}")


def startrun():
    """Run a Student workflow test."""
    a = Student("x", "")
    a.add_grade(100)
    a.add_grade("Fifty")  # broken
    a.calc_average()
    a.is_honor_roll()
    a.delete_grade(5)  # IndexError
    a.report()


startrun()
