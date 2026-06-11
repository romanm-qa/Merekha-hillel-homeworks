class Student:

    def __init__(self, name, surname, age, average_grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_grade = average_grade

    def change_grade(self, new_grade):
        self.average_grade = new_grade

    def show_info(self):
        print(
            f"Name: {self.name}, "
            f"Surname: {self.surname}, "
            f"Age: {self.age}, "
            f"Average grade: {self.average_grade}"
        )


qa_student = Student("Roman", "Merekha", 29, 100)

print("Before grade change:")
qa_student.show_info()

qa_student.change_grade(30)

print("\nAfter grade change:")
qa_student.show_info()