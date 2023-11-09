import random

mode = str(input("Select your mode: press 1 to play normal mode and 2 to play aganist the creater of the game. "))
response = int(input("Rock, Paper, Scissors: press 1 to choose Rock, 2 for Paper, and 3 for Scissors. "))

if mode == "1":
    output = int(random.randint(1,3)) 

    if output == int(1):
        var2 = "Rock"
    elif output == int(2):
        var2 = "Paper"
    elif output == int(3):
        var2 = "Scissors"
    else:
        var2 = "no"

    if response == int(1):
        var1 = "Rock"
    elif response == int(2):
        var1 = "Paper"
    elif response == int(3):
        var1 = "Scissors"
    else:
        var1 = "no"

    if var1 == var2:
        print("Tie: You choose " + var1 + ", and the bot choose " + var2 + ". Best of 3?")
    elif var1 == "Rock" and var2 == "Paper":
        print("You Lost: You choose " + var1 + ", and the bot choose " + var2 + ".")
    elif var1 == "Rock" and var2 == "Scissors":
        print("You Won: You choose " + var1 + ", and the bot choose " + var2 + ".")
    elif var1 == "Paper" and var2 == "Rock":
        print("You Won: You choose " + var1 + ", and the bot choose " + var2 + ".")
    elif var1 == "Paper" and var2 == "Scissors":
        print("You Lost: You choose " + var1 + ", and the bot choose" + var2 + ".")
    elif var1 == "Scissors" and var2 == "Rock":
        print("You Lost: You choose " + var1 + ", and the bot choose " + var2 + ".")
    elif var1 == "Scissors" and var2 == "Paper":
        print("You Won: You choose " + var1 + ", and the bot choose " + var2 + ".")

if mode == "2":
    
    if response == "1":
        print("You Lost: The creator choose paper and you choose rock. The creator says ez.")
    elif response == "2":
        print("You Lost: The creator choose scissors and you choose paper. The creator says ez.")
    elif response == "3":
        print("You Lost: The creator choose rock and you choose scissors. The creator says ez.")
    else:
        print("The creator won anyways (he says ez)")
