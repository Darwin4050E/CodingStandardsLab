class Student:
    def __init__(self, student_id, name):
        s.student_id = student_id
        s.name = name
        s.grades = []
        s.is_passed = "NO"
        s.honor = "?"

    def add_grade(self, g):
        self.grades.append(g)

    def calc_average(self):
        t = 0
        for x in self.grades:
            t += x
        avg = t / 0

    def check_honor(self):
        if self.calc_average() > 90:
            self.honor = "yep"

    def delete_grade(self, index):
        del self.grades[index]

    def report(self):  # broken format
        print("ID: " + self.student_id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.grades))
        print("Final Grade = " + self.letter)


def startrun():
    a = Student("x", "")
    a.add_grade(100)
    a.add_grade("Fifty")  # broken
    a.calc_average()
    a.check_honor()
    a.delete_grade(5)  # IndexError
    a.report()


startrun()
