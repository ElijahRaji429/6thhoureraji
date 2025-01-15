#Name: Elijah Raji
#Class:6th hour
#Assinment:hw15
import random
#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".
def rock_paper_scissors():
    rock = 1
    paper = 2
    scissors = 3
    playernum = int(input("choose 1 for rock, 2 for paper, 3 for scissors"))
    compnumb = random.randint(1,3)
    print("Opponent got ", compnumb)
    if playernum == 1 and compnumb == 2:
        print("computer wins!")
    elif playernum == 2 and compnumb == 3:
        print("computer wins!")
    elif playernum == 3 and compnumb == 1:
        print("computer wins!")
    if playernum == 2 and compnumb == 1:
        print("you win!")
    elif playernum == 3 and compnumb == 2:
        print("you win!")
    elif playernum == 1 and compnumb == 3:
        print("you win!")
    if playernum == 1 and compnumb == 1:
        print("its a tie!")
    elif playernum == 2 and compnumb == 2:
        print("its a tie!")
    elif playernum == 1 and compnumb == 1:
        print("its a tie!")


rock_paper_scissors()
#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.
replayInput = input("Would like to play again? Y/N")
def game_repeat():
    if replayInput == "Y":
        rock_paper_scissors()
    elif replayInput == "N":
        exit()

rock_paper_scissors()