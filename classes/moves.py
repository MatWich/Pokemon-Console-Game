from classes.colors import bcolors, WATER, FIRE, ELECTRIC, GRASS, ROCK
import random

class Moves:
    def __init__(self, name, dmg, type, purpose):
        self.name =  name
        self.Ldmg = dmg - 10
        self.dmg = dmg
        self.Hdmg = dmg + 10
        self.type = type
        self.purpose = purpose


    def getDamageValue(self):
        return self.dmg

    def generateDamageMult(self):
        
        if self.dmg < 10:
            return random.randrange(1, 5)

        elif self.dmg == 35:
            return 1

        elif self.dmg == 50:
            return 1.25

        elif self.dmg == 80:
            return 1.5

        elif self.dmg == 100:
            return 2

    def generateBuffDamage(self):
        return random.randrange(self.dmg - 2, self.dmg + 2)

    #czy ma przewage
    def isDominant(self, pokemon):
        if self.type == FIRE and pokemon.type == GRASS:
            return True
        elif self.type == WATER and pokemon.type == FIRE:
            return True
        elif self.type == GRASS and pokemon.type == WATER:
            return True
        elif self.type == ROCK and pokemon.type == ELECTRIC:
            return True
        elif self.type == WATER and pokemon.type == ROCK:
            return True
        elif self.type == GRASS and pokemon.type == ELECTRIC:
            return True
        elif self.type == ELECTRIC and pokemon.type == WATER:
            return True
        else:
            return False