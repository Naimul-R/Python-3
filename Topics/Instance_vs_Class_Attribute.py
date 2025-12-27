class Employee:
    language = "Python" #This is a class Attribute
    Expertice = "CyberSecurity"
    selary = 1200000

#Instance Attribute take preference over the class attribute during assingment & retrival

Naimul = Employee()
Naimul.language = "JavaScript" #This/name is a instance Attribute
print(Naimul.language, Naimul.Expertice, Naimul.selary)


##self parameter-->
class Employee:
    language = "Python" 
    Expertice = "CyberSecurity"
    selary = 1200000

    def getInfo(self):
        print(f"The language is: {self.language}. The selary is: {self.selary}")

    def Greet(self, name):
        # self.name = "Naimul",
        print(f"Good Morning {name}")

    @staticmethod
    def Bye():
        print("Have a great day Mr.")

Naimul = Employee()
Naimul.language = "JavaScript" 
Naimul.Greet(name="Naimul")
Naimul.getInfo()
# Employee.getInfo(Naimul)