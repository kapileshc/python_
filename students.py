

class Students:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade


class Course:
    def __init__(self,course):
        self.course = course
        self.students = []

    def add_students(self,student):
        self.students.append(student)

    def get_students(self):
        return self.students

