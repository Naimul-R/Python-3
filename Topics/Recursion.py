'''This is Factorial->>
factorial (0) = 1
factorial (1) = 1
factorial (2) = 2 x 1
factorial (3) = 3 x 2 x 1
factorial (4) = 4 x 3 x 2 x 1
factorial (5) = 5 x 4 x 3 x 2 x 1
factorial (n) = n x (n-1) x.......3 x 2 x 1

Formula:-
factoral (n) = n * factorial (n - 1)

'''

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    return n * factorial (n-1)

n = int(input("Enter a number: "))
print (f"This is factorial number: {factorial(n)}")


##Fctorial using Iterative methods-->
def factorial_iteretive (n):
    fact = 1
    for i in range (n):
        fact = fact * (i+1)
    return fact

##Factorial using recursive methods-->
def factorial_recursive (n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive (n-1)

number = int(input("Enter the number: "))

print (f"Factorial using Iterative method", factorial_iteretive(number))
print (f"Factorial using Recursive method", factorial_recursive(number))

