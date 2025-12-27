try:
    n = int(input("Enter a number: "))
    print(f"Integer value is: {n}")
except ValueError:
    print("Value is Not Integer")

#Another way to handle exception
try:
    n = int(input("Enter a number: "))
except ValueError:
    print("Value is Not Integer")
else:
    print(f"Integer value is: {n}")