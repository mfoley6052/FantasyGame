#Mitchell Foley
import Human
import Position
import Monster
import random

#Variables
running = False
#Arrays
enemy= []

def startUp():
    random.seed()
    running = True
    armLeft = Position.position(0,"")
    armRight = Position.position(0,"")
    back = Position.position(0,"")
    backpack = []
    back.equip("backpack")
    for i in range(12):
        backpack.append(Position.position(0,""))
    Player = Human.Human(raw_input("Enter your character's name: "),input("Enter your character's age: "),input("Is your character 1) male 2) female?"),50,3,200,5)

def genEnemy():
    enemy.append(Monster(0.15*Player.getHP(),5,300))

def cleanUp():
    #close any graphics windows
    #close any files
    exit

def update():
    #update display
    #called repeatedly

    if Player.isDead():
        running = False

    

#Game Sequence
startUp()
#while running:
#    update()
#cleanUp()
