'''
classes: Tree, Gnome, Woodchuck, Garden
water gauge
chance of rain
chance of tree disappearing
each turn: rain or woodchuck

'''

import random
from unicodedata import name

# Classes
class Tree:
    def __init__(self):
        self.shade = -2
        

class Woodchuck:
    def __init__(self):
        self.disappearingTreeChance = 5
        
  
class Gnome: 
    def __init__(self):
        self.rainChance = 5


class Garden:
    def __init__(self):
        self.trees = []
        self.woodchucks = []
        self.gnomes = []
        self.squirrels = []
        self.waterLevel = 0
        self.waterLoss = 20
        self.rainChance = 40
        self.woodchuckChance = 10
        self.disappearingTreeChance = 0
        self.squirrelChance = 10
        self.fruitLossChance = 0


# Functions        
    def addTree(self):
        tree = Tree()
        self.trees.append(tree)
        
    def addGnome(self):
        gnome = Gnome()
        self.gnomes.append(gnome)
        self.rainChance += gnome.rainChance
        
    def addWoodchuck(self):
        woody = Woodchuck()
        self.woodchucks.append(woody)
        self.disappearingTreeChance += woody.disappearingTreeChance
    
    def addSquirrel(self):
        squirrel = Squirrel()
        self.squirrels.append(squirrel)
        self.fruitLossChance += squirrel.fruitDecreaseChance

    def rain(self):
        self.waterLevel += 40
        self.fruitTree.fruitTreeWaterCounter += 40
    
    def createFruitTree(self):
        self.fruitTree = FruitTree()

    def loseWater(self):
        decrease = ourGarden.waterLoss - ((len(ourGarden.trees) * 2 + 2))
        ourGarden.waterLevel -= decrease
        if ourGarden.waterLevel < 0:
            ourGarden.waterLevel = 0

# Bonus
class FruitTree(Tree):
    def __init__(self):
        self.numFruit = 0
        self.fruitTreeWaterCounter = 0

    def addFruit(self):
        self.numFruit += 1
    
    def resetWaterCounter(self):
        self.fruitTreeWaterCounter = 0
        
class Squirrel:
    def __init__(self):
        self.fruitDecreaseChance = 5
        

# Simulation loop
ourGarden = Garden()
ourGarden.createFruitTree()

i = 1
#fruitTreeCounter = 0
newTree = 0
rainChance = ourGarden.rainChance
while len(ourGarden.trees) < 10 and ourGarden.fruitTree.numFruit < 10: # and ourGarden.waterLevel > 0:
    print('\n\nRound %d' % i)
    print('**********************************************')
    #seeing if it will rain
    chance = random.random() * 100
    if chance < rainChance:
        ourGarden.rain()
        newTree += 1
        print('It rained! Water levels increased.')

    #seeing if a new tree was added to the garden
    if newTree % 4 == 0 and newTree > 0:
        ourGarden.addTree()
        print('A new tree has blossomed!')

    #seeing if a woodchuck was added to the garden
    chance = random.random() * 100
    if chance < ourGarden.woodchuckChance:
        ourGarden.addWoodchuck()
        print('A pesky woodchuck has entered the garden!')

    #seeing if a woodchuck has destroyed a tree
    chance = random.random() * 100
    if chance < ourGarden.disappearingTreeChance and len(ourGarden.trees) > 0:
        del ourGarden.trees[0]
        print('The woodchucks destroyed a tree!')

    #every ten rounds see if a tree or a gnome was added to the garden
    if i % 10 == 0:
        chance = random.random() * 100
        if chance > 50:
            ourGarden.addTree()
            print('A new tree has blossomed')
        else:
            ourGarden.addGnome()
            print('The garden has been blessed with a new gnome!')

    #seeing if a new fruit will grow on the fruit tree
    if ourGarden.fruitTree.fruitTreeWaterCounter > 100:
        ourGarden.fruitTree.addFruit()
        print('A new fruit has grown on the Fruit Tree!')
        ourGarden.fruitTree.resetWaterCounter()

    #seeing if a squirrel was added to the garden
    chance = random.random() * 100
    if chance < ourGarden.squirrelChance:
        ourGarden.addSquirrel()
        print('A squirrel has found its way into the garden!')

    #seeing if a squirrel has destroyed a fruit
    chance = random.random() * 100
    if chance < ourGarden.fruitLossChance and ourGarden.fruitTree.numFruit > 0:
        ourGarden.fruitTree.numFruit -= 1
        print('The squirrels have eaten a fruit!')
        
    # decrease waterlevel based on number of trees there are
    ourGarden.loseWater()

    #print statements
    print('**********************************************')
    print('Water Level: %d' % ourGarden.waterLevel)
    print('Trees: %d' % len(ourGarden.trees))
    print('Gnomes: %d' % len(ourGarden.gnomes))
    print('Woodchucks: %d' % len(ourGarden.woodchucks))
    print('Squirrels: %d' % len(ourGarden.squirrels))
    print('Fruits: %i ' % ourGarden.fruitTree.numFruit)
    
    #break out of while loop because the garden has been overrun by squirrels and woodchucks
    if len(ourGarden.woodchucks) >= 15 and len(ourGarden.squirrels) >= 15:
        break

    input('Enter a key to continue: ')
    i += 1
# end while loop


# Win and lose conditions
if len(ourGarden.trees) >= 10 or ourGarden.fruitTree.numFruit >= 10:
    print('You have won!')
elif len(ourGarden.woodchucks) >= 11 and len(ourGarden.squirrels) >= 11:
    print('Your garden has been overrun by creatures')

