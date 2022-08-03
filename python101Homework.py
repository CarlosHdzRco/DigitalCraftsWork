import random

def coinFlip():
    randNum = random.randint(0,1)

    print("You flipped a coin!")

    if randNum == 0:
        print("It is heads")
    else:
        print("It is tails")

coinFlip()

def evenOdd():
    numInput = input("Please enter a number: ")

    while numInput.isdigit() == False:
        numInput = input('Please enter a number: ')
    
    numInput = int(numInput)
    if numInput % 2 == 0:
        print('Number is even')
    else:
        print('Number is odd')

evenOdd()


inputNum = input("How many sides should it have? (2-20): ")

while inputNum.isdigit() == False or int(inputNum) > 20 or int(inputNum) < 2:
    inputNum = input("How many sides should it have? (2-20): ")

inputNum = int(inputNum)

def diceRoller(firstNum, secondNum):
    numRolled = random.randint(firstNum, secondNum)
    print("It's rolling...\nIt's a %i" % numRolled)

diceRoller(1, inputNum)
    