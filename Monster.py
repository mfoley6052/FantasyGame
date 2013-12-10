#Mitchell Foley
from random import *
class monster():

    def __init__(self,health,armour,mana):
        self.HP = health
        self.armour = armour
        self.mana = mana

    def damage(self,chance,crit,dmg):
        doesCrit = bool(random() <= chance)
        if doesCrit:
            self.HP -= crit*dmg-self.armour
        else:
            self.HP -= dmg-self.armour

    #def destroy(self):
        #erase from arrays
        # quit any recurring events

    def cast(self,spell,cost,chance):
        if self.mana >= cost:
            if random.randint(0,chance) != 0:
                self.mana -= cost
                return 1 #spell success
            return 0 #spell missed
        else:
            return 0 #spell failed

    
