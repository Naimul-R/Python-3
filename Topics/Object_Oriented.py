#Creating Class in OOP-->
class Employee:
    language = "Python" #This is a class Attribute
    Expertice = "CyberSecurity"
    selary = 1200000

# Here name is instance Attribute, selary and language is class Attribute 
# as they direct belong to class attribute-->

Naimul = Employee()
Naimul.name = "Naimul" #This/name is a instance Attribute
print(Naimul.name, Naimul.Expertice, Naimul.selary)

Sahariar = Employee()
Sahariar.name = "Sahariar"
print(Sahariar.name, Sahariar.language, Sahariar.selary)