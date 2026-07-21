#Create a class Dog with attributes name and breed using __init__.Create two dog objects and print their info.
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def dog_info(self):
        print(f"The dog's name is {self.name}. It's a {self.breed}")
    #Add a method bark() to the Dog 
    # class that prints "<name> says Woof!".
    def bark(self):
        print(f"{self.name} says Woof!")
s1 = Dog("Toby", "German Shepherd")
s1.dog_info()
s1.bark()
