l = ["Red", "shirt", "shoes", "Jacket", "pants"]

for iteam in l:
    print(iteam)

else:
    print("you are good to go")

##Break condition in loops
# for i in range(100):
#     if (i == 51):
#         break #exit the loop right now.
#     print(i)

##Continue condition in loop
for i in range(50):
    if (i == 25):
        continue #skip the itretion
    print(i)

##Pass statement
for i in range(500):
    pass #we can work here after by giving statement "pass"

i = 0
while (i < 10):
    print(i)
    i += 1