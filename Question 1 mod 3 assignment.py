'''Q1. Create a Python class representing a student with attributes such as name and ID, and include both a default constructor and a parameterized constructor. 
Add a method to display the student details, and use the pass statement inside an empty placeholder method. Then create multiple objects from this class to test each constructor.'''

class Student:
  def __init__(self, name = "Unnamed", id = 0):
    self.name = name
    self.id = id
  def student_information(self):
    return f"The Students name is {self.name}. ID = {self.id}"
  def new_admission(self):
    pass
s1 = Student()
s2 = Student("Munib", 200302066)
s3 = Student("Moumachi", 200406062)

print(s1.student_information())
print(s2.student_information())
print(s3.student_information())
