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

# Function that draws pokemon for players
def GiveAway(list):
    p1List = []
    p2List = []
    whoGets = 0
    for i in range(0, 4):
        choice = secrets.choice(list)
        if whoGets == 0:
            p1List.append(choice)
            index = list.index(choice)
            del list[index]
            whoGets += 1
        elif whoGets == 1:    
            p2List.append(choice)
            index = list.index(choice)
            del list[index]
            whoGets = 0
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
Growl = Moves("Growl", 2, NORMAL, 'ATK_debuff')
# Pokemon
bigHungus = bcolors.OKGREEN + 'Big Hungus' + bcolors.ENDC
poke2 = Pokemon(bigHungus, GRASS, 22, 8, 10, 2, 10, 3, [Scratch, Growl, Recovery, RazorLeaf])

Shaggy = bcolors.OKGREY + 'Shaggy' + bcolors.ENDC
poke1 = Pokemon(Shaggy, FIRE, 20, 12, 9, 14, 1, 6, [LeafPunch, WaterPunch, ThunderPunch , FirePunch])

SpongeBob = bcolors.OKYELLOW + 'SpongeBob' + bcolors.ENDC
poke3 = Pokemon(SpongeBob, ELECTRIC, 20, 5, 13, 15, 1, 4, [Scratch, Growl, waterGun, HydroPomp])

Shrekku = bcolors.OKGREEN + 'Shrekku' + bcolors.ENDC
poke4 = Pokemon(Shrekku, GRASS, 23, 1, 12, 15, 3, 5, [Recovery, DefenceCurl, HydroPomp, LeafPunch] )

Rick = bcolors.OKYELLOW + 'Rick' + bcolors.ENDC
poke5 = Pokemon(Rick, ELECTRIC, 20, 1, 5, 17, 10, 4, [ThunderBolt, Flamethrower, ThunderPunch, Recovery])

Morty = bcolors.OKBLUE + 'Morty' + bcolors.ENDC
poke6 = Pokemon(Morty, WATER, 19, 12, 10, 1, 5, 8, [VineWhip, LeafPunch, RazorLeaf, Recovery])

PokemonList = [poke1, poke2, poke3, poke4, poke5, poke6]

# Player's Pk
YoursPk, EnemysPk = GiveAway(PokemonList)
 

# Player's n stuff
strPlayer1 = bcolors.OKRED + 'Ash' + bcolors.ENDC
Player1 = Player(strPlayer1, 100, YoursPk, Player1Set)

strPlayer2 = bcolors.OKBLUE + 'Gary' + bcolors.ENDC
Player2 = Player(strPlayer2, 999, EnemysPk, Player2Set)

delayPrint(Player2.name + ' wants to fight!')

#MainLoop
run = True
while run:

    # PLAYER1'S TURN
    # Checking winning conditions
    Player1.Lose(Player2)
    # wypisanie statystyk LP
    
    print('\n' + bcolors.BOLD + Player1.name +" Pk:" + bcolors.ENDC)
    for poke in Player1.pokemonQuantity:
        poke.printHp()
    print('\n')

    for Pk in Player1.pokemonQuantity:
        
        # wybranie akcji
        Pk.ChooseAction()
        choice = int(input('Choose action: '))
        
        # wypisanie atakow
        if choice == 1:
            # Choosing atk
            Pk.ChooseAttack()
            atkChoice = int(input('Choose atk: ')) - 1

            # Choosing enemy
            enemy = Pk.chooseTarget(Player2.pokemonQuantity)
            notEnemy = Player1.pokemonQuantity.index(Pk)
            PLayer1, Player2 = Player1.PokemonDamageCalculation(Player2, notEnemy, enemy, atkChoice)

            
        # ITEMS
        elif choice == 2:
            #choosing items
            Player1.chooseItem()
            itemChoice = int(input('Choose item: \n-1 to back to actions\n')) - 1
            item = Player1.items[itemChoice]["item"]

            if Player1.items[itemChoice]["quantity"] == 0:
                print(bcolors.BLINK + "\n" + "None of that left :(" + bcolors.ENDC)
                continue
            Player1.items[itemChoice]["quantity"] -= 1

            if item.type == "potion":
                for pk in Player1.pokemonQuantity:
                    pk.printHp()
                pkChoice = int(input('Wchich should be healed?: ')) - 1
                Player1.pokemonQuantity[pkChoice].heal(item.prop)
                print(bcolors.OKGREEN + '\n' + item.name + " heals for", str(item.prop), " HP " + Player1.pokemonQuantity[pkChoice].name + bcolors.ENDC)
            
            elif item.type == "weapon":
                for pk in Player2.pokemonQuantity:
                    pk.printHp()
                pkChoice = int(input('Which of them should receive a damage?: ')) - 1
                Player2.pokemonQuantity[pkChoice].takeDamageNormal(item.prop)
                print(bcolors.OKRED + '\n' + item.name + "  deals ", str(item.prop), " damage" + Player2.pokemonQuantity[pkChoice].name + bcolors.ENDC)

            # Jesli padl to usuwany jest 
            if Player2.pokemonQuantity[pkChoice].getHp() == 0:
                print(Player2.pokemonQuantity[pkChoice].name.replace(" ", "") + ' has died.')
                del Player2.pokemonQuantity[pkChoice]    
        
        # RUN BERRY RUN
        elif choice == 3:
            print(bcolors.BOLD + 'YOU ESCAPED' + bcolors.ENDC)
            exit(0)
        
        else:
            print('There is no option ', choice)
            break

    # ENEMY's TURN
    #Checking winning conditions
    Player2.Lose(Player1)    
    # wypisanie stanu LP    
    print('\n' + bcolors.BOLD + Player2.name +" Pk:" + bcolors.ENDC)
    
    for Pk in Player2.pokemonQuantity:
        Pk.printHp()

    for Pk in Player2.pokemonQuantity:
        

        #wybor akcji
        Pk.ChooseAction()
        choice = int(input('Choose action: '))
        
        # wypisanie atakow
        if choice == 1:
            Pk.ChooseAttack()
            atkChoice = int(input('        Choose attack: ')) - 1
            
            enemy = Pk.chooseTarget(Player1.pokemonQuantity)
            notEnemy = Player2.pokemonQuantity.index(Pk)
            Player2, PLayer1 = Player2.PokemonDamageCalculation(Player1, notEnemy, enemy,atkChoice)



        # ITEMS
        elif choice == 2:
            #choosing items
            Player2.chooseItem()
            itemChoice = int(input('Choose item: \n-1 to back to actions\n')) - 1
            item = Player2.items[itemChoice]["item"]

            if Player2.items[itemChoice]["quantity"] == 0:
                print(bcolors.BLINK + "\n" + "None of that left :(" + bcolors.ENDC)
                continue
            Player2.items[itemChoice]["quantity"] -= 1

            if item.type == "potion":
                for pk in Player2.pokemonQuantity:
                    pk.printHp()
                pkChoice = int(input('Wchich should be healed?: ')) - 1
                Player2.pokemonQuantity[pkChoice].heal(item.prop)
                print(bcolors.OKGREEN + '\n' + item.name + " heals for", str(item.prop), " HP " + Player2.pokemonQuantity[pkChoice].name + bcolors.ENDC)
            
            elif item.type == "weapon":
                for pk in Player1.pokemonQuantity:
                    pk.printHp()
                pkChoice = int(input('Which of them should receive a damage?: ')) - 1
                Player1.pokemonQuantity[pkChoice].takeDamageNormal(item.prop)
                print(bcolors.OKRED + '\n' + item.name + "  deals ", str(item.prop), " damage" + Player1.pokemonQuantity[pkChoice].name + bcolors.ENDC)

            # Jesli padl to usuwany jest 
            if Player1.pokemonQuantity[pkChoice].getHp() == 0:
                print(Player2.pokemonQuantity[pkChoice].name.replace(" ", "") + ' has died.')
                del Player1.pokemonQuantity[pkChoice]
        
        elif choice == 3:
            print(bcolors.BOLD + 'YOU ESCAPED' + bcolors.ENDC)
            exit(0)
        
        else:
            print('There is no option ', choice)
            continue
    
