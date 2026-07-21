'''Q3: Define a class that shows encapsulation by using private attributes and public getter/setter methods. 
Add two methods with the same name but different parameter counts to illustrate method overloading (using default arguments). 
Then create another class to demonstrate multiple inheritance.'''
class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance

    # Getter
    def get_balance(self):
        return self.__balance

    # Setter
    def set_balance(self, amount):
        if amount < 0:
            print("Balance can't be negative.")
        else:
            self.__balance = amount

    #Method overloading
    def deposit(self, amount, bonus=0):
        self.__balance += amount + bonus
        return self.__balance


#Multiple inheritance
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"I'm {self.name}."


class Employee:
    def __init__(self, salary):
        self.salary = salary

    def show_salary(self):
        return f"My salary is {self.salary}."


class Manager(Person, Employee):
    def __init__(self, name, salary, department):
        Person.__init__(self, name)
        Employee.__init__(self, salary)
        self.department = department

    def introduce(self):
        return f"I'm {self.name}, managing the {self.department} department."


#Testing
acc = BankAccount("Munib", 1000)
print(acc.get_balance())
acc.set_balance(1500)
print(acc.get_balance())
print(acc.deposit(200))
print(acc.deposit(200, 50))

m = Manager("Rafiq", 60000, "Sales")
print(m.introduce())
print(m.show_salary())
