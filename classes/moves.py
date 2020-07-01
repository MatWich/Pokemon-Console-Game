from classes.colors import bcolors, WATER, FIRE, ELECTRIC, GRASS, ROCK
import random

class Moves:
    def __init__(self, name, dmg, type, purpose):
        self.name =  name
        self.Ldmg = dmg - 10
        self.Hdmg = dmg + 10
        self.type = type
        self.purpose = purpose


    def generateDamage(self):
        return random.randrange(self.Ldmg, self.Hdmg)

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
        else:
            return False