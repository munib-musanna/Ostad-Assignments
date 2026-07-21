'''8. (Challenge) Create a parent class Person (with name and a greet()
method) and a child class Employee that inherits from it and
adds a work() method. Show that an Employee object can both
greet and work'''

class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return f"Hello, {self.name}. How are you?"
class Employee(Person):
    def __init__(self,name, job_title):
        super().__init__(name)
        self.job_title = job_title
    def work(self):
        return f"{self.name} works as a/an {self.job_title}"
s1 = Employee("Abdul", "Janitor")

print(s1.work())
print(s1.greet())
