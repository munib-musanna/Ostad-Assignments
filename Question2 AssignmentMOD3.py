'''Q2. Write a Python program demonstrating single, multilevel, and hierarchical inheritance using simple classes such as Person, Student, and Teacher. Include at least one overridden method in the child classes to show method overriding.'''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def greet(self):
    return f"Hi, {self.name}. Are you {self.age} years old?"
p1 = Person("Munib", 23)
print(p1.greet())

class Student(Person):
  def __init__(self, name, age, discipline):
    super().__init__(name,age)
    self.discipline = discipline
  def greet(self):
    return f"Hi, I'm {self.name}. A student of {self.discipline} discipline."
p2 = Student("Munib", 23, "Science")
print(p2.greet())

class Teacher(Person):
  def __init__(self, name, age, designation):
    super().__init__(name,age)
    self.designation = designation
  def greet(self):
    return f"Hi, I'm {self.name}. I'm the {self.designation} of Munib."

p3 = Teacher("Afaz", 39, "Class Teacher")
print(p3.greet())

class Grad_Student(Student):
  def __init__(self, name, age, discipline, project_topic):
    super().__init__(name,age,discipline)
    self.project_topic = project_topic
  def greet(self):
    return f"I'm {self.name}. I come from {self.discipline} background. Currently working on {self.project_topic}"
p4 = Grad_Student("Sharif",29,"Science", "Dark Matter")
print(p4.greet())
