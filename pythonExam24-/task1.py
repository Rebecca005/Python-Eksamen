class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def print_info(self):
        print(f"Full Name: {self.fname} {self.lname}")
        print(f"Age: {self.age}")


class Student(Person):
    def __init__(self, fname, lname, age, student_id):
        super().__init__(fname, lname, age)
        self.student_id = student_id

    def print_stuinfo(self):
        super().print_info()
        print("Student ID:", self.student_id)


class Employee(Person):
    def __init__(self, fname, lname, age, employee_nr, salary):
        super().__init__(fname, lname, age)
        self.employee_id = employee_nr
        self.salary = salary

    def print_empinfo(self):
        super().print_info()
        print("Employee Number:", self.employee_id)
        print("Salary:", self.salary)


new_student = Student("Anthony", "Smith", 35, "s346571")
new_student.print_stuinfo()
print("==========================")
new_employee = Employee("Sarah", "Taylor", 34, 2919736, "5000 USD")
new_employee.print_empinfo()
