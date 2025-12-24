try:
    a = int(input("Enter a number: "))
    print (a)

except ValueError as v:
    print ("Heyy")
    print (v)

except Exception as e:
    print (e)

print ("Done")

##Rising Espection
a = int(input("Enter a Number: "))
b = int(input("Enter snd Number: "))

if (b == 0):
    raise ZeroDivisionError ("Hey our programme is not meant to devide number by zero")
else:
    print(f"The devision a/b is {a/b}")