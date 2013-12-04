#Mitchell Foley
import random
class Human():

    def __init__(self,name,age,gender,health,armour,mana,regen):
        self.HP = health
        self.name = name
        self.age = age
        self.gender = gender
        self.armour = armour
        self.mana = mana
        self.regen = regen

    def damage(self,chance,crit,dmg):
        doesCrit = False
        #determine if actually crits
        if doesCrit:
            self.HP -= crit*dmg-self.armour
        else:
            self.HP -= dmg-self.armour

    def isDead(self):
        if self.HP <= 0:
            print "Dead"
            self.destroy()

    def sleep(self,time):
        if time >= 12:
            self.HP += (self.regen+2)*time
        elif time >= 8:
            self.HP += (self.regen+1)*time
        elif time >= 4:
            self.HP += self.regen*time
        else:
            self.HP += (self.regen-2)*time

    def pickup(self,item,spot):
        if spot.getState() == 0:
            spot.equip(item)
        else:
            return "No room in spot"

    def destroy(self):
        return True

    def cast(self,spell,cost,chance):
        if self.mana >= cost:
            if random.randint(0,chance) != 0:
                self.mana -= cost
                return 1 #spell success
            return 0 #spell missed
        else:
            return 0 #spell failed

    def getHP(self):
        return self.HP
