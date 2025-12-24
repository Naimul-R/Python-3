#Functions --
# def avg():  #Function defination
#     a = int(input("Enter number: "))
#     b = int(input("Enter number: "))
#     c = int(input("Enter number: "))

#     avarage = (a + b + c)/3
#     print(avarage)

# avg() #Function call 
# avg()
# avg()

#Type of function--
#1- build in function (define by pyton like, len(), print())
#2- user defined function (define by user)


##Function with arguement:--
def GoodDay(name, like):
    print("Good day " + name)
    print(like)

GoodDay("Naimul", "Sports")

##concept of return value:--
def GoodDay(name, greet):
    print("Good day " + name)
    print(greet)
    return "Okey"

a = GoodDay("Naimul", "Thanks")
print(a)

##Default arguement:-
def Amazing (name, ending="Thank you"): #by defult arguements use this "Thank you"
    print(f"Good Morning, {name}")
    print(ending)

Amazing("Naimul")
