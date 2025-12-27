#Dictonary is a mutable data stracture
marks = {
    "list": ["Phy", "chem", "math", "ICT"],
    "Naimul" : 99,
    "Ekra" : 88,
    "Mim": 75,
    "Abbas": 89
}

# print (marks, type(marks))
# print(marks["list"])
# print(marks["Naimul"])

#methods:

# print(marks.items())
# print(marks.keys())
# print(marks.values())
marks.update({"Ekra": 98, "Aysha": 68}) #Mutable/Changeable by this methods.
print(marks)

# Get = marks.get("Ekra")
# print(Get)

Mim = marks.pop("Mim")
print(Mim)
print(marks)