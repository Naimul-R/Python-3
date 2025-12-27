import random

ROCK = "r"
SECISSOR = "s"
PAPER = "p"
Emojis = {ROCK: "🪨", SECISSOR: "✂️", PAPER: "📃"}
choices = ("r", "p", SECISSOR)

def get_user_choice():
    while True:
        User_choice = input("Rock, paper, scissors? (r/p/s): ").lower()
        if User_choice in choices:
            return User_choice 
        else:
            print("Invalid Choice!")

def display_choices(User_choice, computer_choices):
     print(f'you chose {Emojis[User_choice]}')
     print(f'computer_chose {Emojis[computer_choices]}')

def determine_winner(User_choice, computer_choices):

    if computer_choices == User_choice:
        print("Tie!!")
    elif(
        (User_choice == ROCK and computer_choices == SECISSOR) or
        (User_choice == SECISSOR and computer_choices == PAPER) or
        (User_choice == PAPER and computer_choices == ROCK)):
        print("you win")
    else:
        print("you lose")

def play_game():
    while True:
        User_choice = get_user_choice()
        computer_choices = random.choice(choices)

        display_choices(User_choice, computer_choices)
        
        determine_winner(User_choice, computer_choices)

        should_continue = input("Continue? (y/n): ").lower()
        if should_continue == "n":
            break

play_game()