class Employee:
    language = "Python" 
    Expertice = "CyberSecurity"
    selary = 1200000
    
    #Dunder methods which is autometically called-->

    def __init__(self, name, selary, language): #Dunder method 
        self.name = name
        self.selary = selary
        self.language = language
        print("I am creating an Object")

    def getInfo(self):
        print(f"The language is: {self.language}. The selary is: {self.selary}")

    def Greet(self, name):
        print(f"Good Morning {name}")

    @staticmethod
    def Bye():
        print("Have a great day Mr.")

Naimul = Employee("Naimul", 1500000, "JavaScript")
# Naimul.name = "Naimul"
Naimul.Greet(name="Naimul")
print(Naimul.name, Naimul.selary, Naimul.language)

# Maliha = Employee() #Here dunder method will call again