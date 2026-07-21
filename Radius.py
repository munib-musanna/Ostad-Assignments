'''Create a class circle with a radius 
and a method area() thar returns 
3.1416 * radius**2'''

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.1416*self.radius**2

s2 = Circle(12)
print(s2.area())

