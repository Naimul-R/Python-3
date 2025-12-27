'''
1 for snake 
-1 for water
0 for gun
'''
import random

computer = random.choice([-1, 1, 0])
youstr = input("Enter your choice: ")
you_dic = {"s": 1, "w": -1, "g": 0}
reverse_dic = {1 : "Snake", -1 : "Water", 0 : "Gun"}

you = you_dic[youstr]

print(f"You choose {reverse_dic[you]}\nComputer choose {reverse_dic[computer]}")

if (computer == you):
    print("It's a draw")


else:
    if (computer == -1 and you == 1):
        print("You win")

    elif (computer == -1 and you == 0):
        print("You lose")

    elif (computer == 1 and you == -1):
        print("You lose")

    elif (computer == 1 and you == 0):
        print("You win")

    elif (computer == 0 and you == -1):
        print("You win")

    elif (computer == 0 and you == 1):
        print("You lose")

    else: 
        print("Something went wrong!!")