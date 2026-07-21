'''Create a class Student with name and marks.
Add a method result() that returns "Pass" if marks
are 40 or above, otherwise "Fail".'''

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def result(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"
s3 = Student("Karim", 45)
print(s3.result())
