'''Create a class whose constructor uses 
default values (name="Guest", age=0).Make 
one object with defaults and one with custom values.'''

class Guest:
    def __init__(self, name = "Guest", age = 0):
        self.name = name
        self.age = age
    def greet(self):
        return f"Hello, {self.name}"

s4 = Guest()
print(s4.greet())

s5 = Guest("Max",45)
print(s5.greet())
