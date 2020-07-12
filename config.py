import sys
import time
import secrets
from classes.colors import bcolors
from classes.colors import WATER, FIRE, GRASS, ROCK, ELECTRIC, NORMAL
from classes.items import Item
from classes.pokemon import Pokemon
from classes.moves import Moves
from classes.player import Player

# Probadly the only function that is familiar with PoKemon Game
def delayPrint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    print('\n')

# Function that draws pokemon for players
def GiveAway(list):
    p1List = []
    p2List = []
    for i in range(0, 4):
        choice = secrets.choice(list)
        if i % 2 == 0:
            p1List.append(choice)
            index = list.index(choice)
            del list[index]
        elif i % 2 == 1:    
            p2List.append(choice)
            index = list.index(choice)
            del list[index]
    return p1List, p2List

# ITEMS
Potion = Item("Potion", "potion", 'This boi regenerate 20 Hp!', 20)
SuperPotion = Item("Super Potion", "potion", 'This boi regenerates 50 Hp!', 50)
HyperPotion = Item("Hyper Potion", "potion", 'This boi regenerates 200 Hp!', 200)

Rock = Item("Rock", "weapon", 'Its kinda works like grenade but not explode n its plenty of it everywhere!', 500)

# ITEMS SETS
Player1Set = [
    {"item": Potion, "quantity": 2},
    {"item": SuperPotion, "quantity": 1},
    {"item": HyperPotion, "quantity": 10},
    {"item": Rock, "quantity": 100}
]

Player2Set = [
    {"item": Potion, "quantity": 1}
]

# MOVES
#FIRE
strEmber = bcolors.OKRED + "Ember" + bcolors.ENDC
Ember = Moves(strEmber, 50, FIRE, 'damageDeal')
strFlamethrower = bcolors.OKRED + "FlameThrower" + bcolors.ENDC
Flamethrower = Moves(strFlamethrower, 100, FIRE, 'damageDeal')
strFirePunch = bcolors.OKRED + "Fire Punch" + bcolors.ENDC
FirePunch = Moves(strFirePunch, 35, FIRE, 'damageDeal')
#WATER
strWaterGun = bcolors.OKBLUE + "Water Gun" + bcolors.ENDC
waterGun = Moves(strWaterGun, 50, WATER, 'damageDeal')
strHydroPomp = bcolors.OKBLUE + "Hydro Pomp" + bcolors.ENDC
HydroPomp = Moves(strHydroPomp, 80, WATER, 'damegeDeal')
strWaterPunch = bcolors.OKBLUE + "Water Punch" + bcolors.ENDC
WaterPunch = Moves(strWaterPunch, 35, WATER, 'damageDeal')
#GRASS
strVineWhip = bcolors.OKGREEN + "Water Punch" + bcolors.ENDC
VineWhip = Moves(strVineWhip, 50, GRASS, 'damageDeal')
strRazorLeaf = bcolors.OKGREEN + "Razar Leaf" + bcolors.ENDC
RazorLeaf = Moves(strRazorLeaf, 80, GRASS, 'damageDeal')
strLeafPunch = bcolors.OKGREEN + "Leaf Punch" + bcolors.ENDC
LeafPunch = Moves(strLeafPunch, 35, GRASS, 'damageDeal')
#ELECTRIC
strThunderBolt = bcolors.OKYELLOW + "Thunder Bolt" + bcolors.ENDC
ThunderBolt = Moves(strThunderBolt, 50, ELECTRIC, 'damageDeal')
strThunder = bcolors.OKYELLOW + "Thunder" + bcolors.ENDC
Thunder = Moves(strThunder, 80, ELECTRIC, 'damgeDeal')
strThunderPunch = bcolors.OKYELLOW + "Thunder Punch" + bcolors.ENDC
ThunderPunch = Moves(strThunderPunch, 35, ELECTRIC, 'damageDeal')
#ROCK
strRockThrow = bcolors.OKGREY + "Rock Throw" + bcolors.ENDC
RockThrow = Moves(strRockThrow, 50, ROCK, 'damageDeal')
strAvalanche = bcolors.OKGREY + "Avalanche" + bcolors.ENDC
Avalanche = Moves(strAvalanche, 80, ROCK, 'damageDeal')
strDefenceCurl = bcolors.OKGREY + "Defence Curl" + bcolors.ENDC
DefenceCurl = Moves(strDefenceCurl, 5, NORMAL, 'DEF_Buff')
#NORMAL
Scratch = Moves("Scratch", 15, NORMAL, 'damageDeal')
Tackle = Moves("Tackle", 15, NORMAL, 'damageDeal')
Recovery = Moves("Recovery", 80, NORMAL, 'HealUp')
Growl = Moves("Growl", 2, NORMAL, 'ATK_Debuff')

# Move Sets
hungusSet = [
    {"move":Scratch, "sp": 2},
    {"move":Growl, "sp": 10},
    {"move":Recovery, "sp":20},
    {"move":RazorLeaf, "sp": 10}
]

shaggySet = [
    {"move":LeafPunch, "sp":5},
    {"move":WaterPunch, "sp":5},
    {"move":ThunderPunch, "sp":5},
    {"move":FirePunch, "sp":5}
]

spongeSet = [
    {"move":Scratch, "sp":2},
    {"move":Growl, "sp":10},
    {"move":waterGun, "sp":10},
    {"move":HydroPomp, "sp":1}
]

rickSet = [
    {"move":ThunderBolt, "sp":2},
    {"move":Flamethrower, "sp":10},
    {"move":ThunderPunch, "sp":10},
    {"move":Recovery, "sp":1}
]

mortySet = [
    {"move":VineWhip, "sp":1},
    {"move":LeafPunch, "sp":5},
    {"move":RazorLeaf, "sp":10},
    {"move":Recovery, "sp":1}
]

shrekuSet = [
    {"move":Recovery, "sp":2},
    {"move":DefenceCurl, "sp":10},
    {"move":HydroPomp, "sp":10},
    {"move":LeafPunch, "sp":5}
]
# Pokemon
bigHungus = bcolors.OKGREEN + 'Big Hungus' + bcolors.ENDC
poke2 = Pokemon(bigHungus, GRASS, 22, 8, 10, 2, 10, 3, hungusSet)

Shaggy = bcolors.OKGREY + 'Shaggy' + bcolors.ENDC
poke1 = Pokemon(Shaggy, FIRE, 20, 12, 9, 14, 1, 6, shaggySet)

SpongeBob = bcolors.OKYELLOW + 'SpongeBob' + bcolors.ENDC
poke3 = Pokemon(SpongeBob, ELECTRIC, 20, 5, 13, 15, 1, 4, spongeSet)

Shrekku = bcolors.OKGREEN + 'Shrekku' + bcolors.ENDC
poke4 = Pokemon(Shrekku, GRASS, 23, 1, 12, 15, 3, 5, shrekuSet)

Rick = bcolors.OKYELLOW + 'Rick' + bcolors.ENDC
poke5 = Pokemon(Rick, ELECTRIC, 20, 1, 5, 17, 10, 4, rickSet)

Morty = bcolors.OKBLUE + 'Morty' + bcolors.ENDC
poke6 = Pokemon(Morty, WATER, 19, 12, 10, 1, 5, 8, mortySet)

PokemonList = [poke1, poke2, poke3, poke4, poke5, poke6]
