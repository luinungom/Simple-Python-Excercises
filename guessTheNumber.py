import random
import sys

numberDiscovered: bool = False
computerNumber: int = random.randint(1,100)
counter: int = 1
while not numberDiscovered:
    try:
        temporalInput = input("Insert a number between 1 and 100: ")
        temporalNumber: int = int(temporalInput)
    except ValueError:
        print('Not a valid value.')
        sys.exit()
    if temporalNumber < 1 or temporalNumber > 100:
        print('Not a valid number.')
    else:
        if temporalNumber == computerNumber:
            numberDiscovered = True
            print('Congratulations, you discovered the secret number!:', computerNumber,'.It took', counter, 'rounds.')
        else:
            counter += 1
            if temporalNumber < computerNumber:
                print('Too low')
            else:
                print('Too high')