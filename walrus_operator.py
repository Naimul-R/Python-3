#using walrus operator
if (n := len([1, 2, 3, 4, 5])) > 3:
    print (f"List is too long ({n} element, expected <= 3)") #output: list is too long 5 element, expected <=3