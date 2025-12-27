#Inheritance in OOP-->
#Inheritance is a way of creating a new class from an existing class.

class Employee: #parant class 
    company = "ITC"
    def show (self):
        print (f"The name of employee is {self.name} and the salary is {self.salary}")


 #here we inheritance programmer within employee.

class programmer (Employee): #derive or child class.
    company = "ITC Infotech"
    def showlanguage(self):
        print (f"The name is {self.name} and he is good in {self.language} language")

a = Employee()
b = programmer()

print(a.company, b.company)


##Multiple Inheritance 
class Employee:
    company = "ITC"
    name = "Default Name"
    def show (self):
        print (f"The name of employee is: {self.name} and the company is: {self.company}")

class coder:
    language = "JavaScript"
    def showlang (self):
        print(f"The language for all is: {self.language}")

class programmer (Employee, coder):
    company = "ITC Infotech"
    def showlanguage(self):
        print (f"The name is {self.company} and he is good in {self.language} language")

a = Employee()
b = programmer()

a.show()
b.showlang()
b.showlanguage()


##Multilevel Inheritance-->>
class Employee:
    def __init__(self):
        print ("Constractor of Employee:")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print ("Constractor of Programmer:")
    b = 2 

class manager(Programmer):
    def __init__(self):
        super().__init__()
        print ("Constractor of manager:")
    c = 3

o = Employee()
print(o.a)

o = Programmer()
print (o.a, o.b)

o = manager()
print(o.a, o.b, o.c)


##classMethod
class Employee:
    a = 10
    @classmethod #Using class method 
    def show (cls):
        print(f"The class Attribute is {cls.a}")

e = Employee()
e.a = 50

e.show()