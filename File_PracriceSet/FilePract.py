import random

def game():
    print("You are playing this game..")
    score = random.randint(2, 100)

    #fetch the HighScore
    with open("D:/project/Pyhton/Practice/File_PracriceSet/highscr.txt") as f:
        highscr = f.read()
        if (highscr != ""):
            highscr = int(highscr)
        else:
            highscr = 0


    print(f"Your score is: {score}")
    if (score > highscr):
        #write this HighScore to the file
        with open("D:/project/Pyhton/Practice/File_PracriceSet/highscr.txt", "w") as f:
            f.write(str(score))

    return score 
game ()