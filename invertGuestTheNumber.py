import random
import sys

# In this version the computer is the one guessing the number selected by the user
numberDiscovered: bool = False
counter: int = 1
firstComputerAttempt: int = 50
numberHighBorder: int = 100
numberLowBorder: int = 1
try:
    playerInput: str = input('Select a number between 1 and 100 that will be found by the computer: ')
    playerNumber: int = int(playerInput)
except ValueError:
    print('Not a valid value.')
    sys.exit()
if playerNumber < 1 or playerNumber > 100:
        print('Not a valid number.')
else:
    while not numberDiscovered:
        if counter == 1:
            print('Computer number is 50')
            if playerNumber == firstComputerAttempt:
                numberDiscovered = True
                print('The computer found the secret number!:', playerNumber,'.It took', counter,
                      'rounds to the machine.')
            else:
                counter += 1
                if firstComputerAttempt < playerNumber:
                    print('Too low')
                    numberLowBorder = 51
                    numberHighBorder = 100
                else:
                    print('Too high')
                    numberLowBorder = 0
                    numberHighBorder = 49
        else:
            computerNumber: int = random.randint(numberLowBorder, numberHighBorder)
            print('Computer number is', computerNumber)
            if playerNumber == computerNumber:
                numberDiscovered = True
                print('The computer found the secret number!:', playerNumber,'.It took', counter,
                      'rounds to the machine.')
            else:
                counter += 1
                if computerNumber < playerNumber:
                    print('Too low')
                    # Adjust the low border for next round
                    numberLowBorder = 1 + computerNumber
                else:
                    print('Too high')
                    # Adjust the high border for next round
                    numberHighBorder = computerNumber - 1