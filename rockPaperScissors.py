import random
import sys

endgame: bool = False
computerOption: int = random.randint(0,2)
numberOfGames: int = 0

print(
    "Welcome to the rock, paper, scissors game! Please select R for rock, P for paper, S for scissors or E for end the game")
while not endgame and numberOfGames != 3:
    playerOption: str = input('rock, paper, scissors, shoot!: ')
    playerOption = playerOption.upper()
    if playerOption == 'E':
        print('Bye!')
        sys.exit()
    if playerOption == 'R' or playerOption == 'P' or playerOption == 'S':
        numberOfGames +=1

    else:
        print('Incorrect value inserted, please try again!')

