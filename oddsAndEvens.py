import random

print('Generating a random value 1 or 2')
numberComputer: int = random.randint(1,2)
valuePlayer: str = input("Insert 1 or 2: ")
if valuePlayer != '1' and valuePlayer !='2':
    print('No valid value inserted')
else:
    numberPlayer: int = int(valuePlayer)
    if (numberPlayer + numberComputer) % 2 == 0:
        print('Even')
    else:
        print('Odd')
    print('Computer selected: ',numberComputer,' and the player selected: ',numberPlayer)