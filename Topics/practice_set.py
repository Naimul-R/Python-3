#problem 1--
# n = int(input("Enter any number: "))
# for i in range(1, 11):
#     print(f"{n}*{i} = {n * i}")
#     i += 1

#problem 3--
# n = int(input("Enter any number: "))

# i = 1
# while (i < 11):
#     print(f"{n} * {i} = {n*i}")
#     i += 1

#problem 2--
# l = ["Naimul", "Ananto", "Naim", "Mahi", "Mahira"]

# for name in l:
#     if (name.startswith("M")):
#         print(f"Hello {name}")

##pattern star --

n = int(input("Enter any number: "))
for i in range(1, n+1):
    print(" "* (n-i), end="")
    print("*"* (2*i-1), end="")
    print("")

#farenhight to celcious-->
def f_to_c (f):
    return 5*(f-32)/9

f = int(input("Enter Temperature in F: "))
c = f_to_c(f)
print(f"{round(c, 2)} °C")
