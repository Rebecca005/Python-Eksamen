class Student:
    passingMark = 50

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def __str__(self):
        return f"Name: {self.name}, Mark: {self.mark}"

    def pass_or_fail(self):
        return f"{self.name} - {'Pass' if self.mark >= Student.passingMark else 'Fail'}"


student1 = Student('John', 52)
status1 = student1.pass_or_fail()
print(status1)

student2 = Student('Jenny', 69)
status2 = student2.pass_or_fail()
print(status2)

print("Updating passing mark to 60")

Student.passingMark = 60

status1 = student1.pass_or_fail()
print(status1)

status2 = student2.pass_or_fail()
print(status2)
