import sys
import time
from classes.colors import bcolors
from classes.colors import WATER, FIRE, GRASS, ROCK, ELECTRIC, NORMAL
from classes.items import Item
from classes.pokemon import Pokemon
from classes.moves import Moves
from classes.player import Player

def delayPrint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

def endMesssage(Player):
    delayPrint(Player.name + ' has won a fight!')
    exit(0)

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
Flamethrower = Moves(strFlamethrower, 80, FIRE, 'damageDeal')
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
Recovery = Moves("Recovery", 80, NORMAL, 'HealUp')
Growl = Moves("Growl", 2, NORMAL, 'ATK_debuff')
# Pokemon
bigHungus = bcolors.OKGREEN + 'Big Hungus' + bcolors.ENDC
poke2 = Pokemon(bigHungus, GRASS, 200, 23, 2, 2, 100, 1, [Flamethrower, waterGun, Recovery, Growl])

Shaggy = bcolors.OKGREY + 'Shaggy' + bcolors.ENDC
poke1 = Pokemon(Shaggy, FIRE, 100, 10, 12, 2, 1, 3, [Scratch, Flamethrower, Recovery, HydroPomp])

SpongeBob = bcolors.OKYELLOW + 'SpongeBob' + bcolors.ENDC
poke3 = Pokemon(SpongeBob, ELECTRIC, 150, 12, 2, 5, 6, 1, [Scratch, Growl, Thunder])

Shrekku = bcolors.OKGREEN + 'Shrekku' + bcolors.ENDC
poke4 = Pokemon(Shrekku, GRASS, 1200, 15, 1, 1, 1, 1, [Recovery, DefenceCurl, Thunder, LeafPunch] )

Rick = bcolors.OKYELLOW + 'Rick' + bcolors.ENDC
poke5 = Pokemon(Rick, ELECTRIC, 300, 50, 1, 30, 1, 4, [ThunderBolt, Flamethrower, ThunderPunch, Recovery])

Morty = bcolors.OKBLUE + 'Morty' + bcolors.ENDC
poke6 = Pokemon(Morty, WATER, 50, 100, 1, 10, 1, 5, [VineWhip, LeafPunch, RazorLeaf, Recovery])

# Players layouts
YoursPk = [poke1, poke4, poke5]
EnemysPk = [poke2, poke3, poke6]

# Player's n stuff
Player1 = Player('Ash', YoursPk, Player1Set)
Player2 = Player('Gary', EnemysPk, Player2Set)

#MainLoop
run = True
while run:
    # PLAYER'S TURN 
    # wypisanie statystyk LP
    print(bcolors.BOLD + "Your's Pk:" + bcolors.ENDC)
    for poke in Player1.pokemonQuantity:
        poke.printHp()
    print('\n')

    for friendlyPk in Player1.pokemonQuantity:
        
        # Sprawdza czy jest jeszcze z kim walczyc
        if Player2.pokemonQuantity == []:
            endMesssage(Player1)

        # wybranie akcji
        friendlyPk.ChooseAction()
        choice = int(input())
        
        # wypisanie atakow
        if choice == 1:

            enemy = friendlyPk.chooseTarget(Player2.pokemonQuantity)
            friendlyPk.ChooseAttack()
            atkChoice = int(input()) - 1


            if friendlyPk.moves[atkChoice].type == NORMAL:
                
                if friendlyPk.moves[atkChoice].purpose == 'damageDeal':
                    dmg = abs(friendlyPk.moves[atkChoice].generateDamage())
                    Player2.pokemonQuantity[enemy].takeDamageNormal(dmg)
                    delayPrint(friendlyPk.moves[atkChoice].name + ' deals '+ str(dmg) + ' damage to ' + Player2.pokemonQuantity[enemy].name + '\n')
                
                elif friendlyPk.moves[atkChoice].purpose == 'ATK_debuff':
                    dmg = abs(friendlyPk.moves[atkChoice].generateDamage())
                    Player2.pokemonQuantity[enemy].getAtkDebuff(dmg)
                    delayPrint(friendlyPk.moves[atkChoice].name + ' decreased attack of ' + Player2.pokemonQuantity[enemy].name + ' by ' + str(dmg) + '\n')
                
                elif friendlyPk.moves[atkChoice].purpose == 'DEF_debuff':
                    dmg = abs(friendlyPk.moves[atkChoice].generateDamage())
                    Player2.pokemonQuantity[enemy].getDefDebuff(dmg)
                    delayPrint(friendlyPk.moves[atkChoice].name + ' decreased defence of ' + Player2.pokemonQuantity[enemy].name + ' by ' + str(dmg) + '\n')
                
                elif friendlyPk.moves[atkChoice].purpose == 'SPD_debuff':
                    dmg = abs(friendlyPk.moves[atkChoice].generateDamage())
                    Player2.pokemonQuantity[enemy].getSpeedDebuff(dmg)
                    delayPrint(friendlyPk.moves[atkChoice].name + ' decreased speeed of ' + Player2.pokemonQuantity[enemy].name + ' by ' + str(dmg) + '\n')
                
                elif friendlyPk.moves[atkChoice].purpose == 'SATK_debuff':
                    dmg = abs(friendlyPk.moves[atkChoice].generateDamage())
                    Player2.pokemonQuantity[enemy].getSattackDebuff(dmg)
                    delayPrint(friendlyPk.moves[atkChoice].name + ' decreased special attack of ' + Player2.pokemonQuantity[enemy].name + ' by ' + str(dmg) + '\n')
                
                elif friendlyPk.moves[atkChoice].purpose == 'SDEF_debuff':
                    dmg = abs(friendlyPk.moves[atkChoice].generateDamage())
                    Player2.pokemonQuantity[enemy].getSdfDebuff(dmg)
                    delayPrint(friendlyPk.moves[atkChoice].name + ' decreased special defence of ' + Player2.pokemonQuantity[enemy].name + ' by ' + str(dmg) + '\n')
                
                elif friendlyPk.moves[atkChoice].purpose == 'HealUp':
                    dmg = abs(friendlyPk.moves[atkChoice].generateDamage())
                    friendlyPk.heal(dmg)
                    delayPrint(friendlyPk.moves[atkChoice].name + ' heals ' + friendlyPk.name + ' by ' + str(dmg) + '\n')
                
                # Buffs
                elif friendlyPk.moves[atkChoice].purpose == 'ATK_Buff':
                    dmg = abs(friendlyPk.moves[atkChoice].generateDamage())
                    friendlyPk.AtkBuff(dmg)
                    delayPrint(friendlyPk.moves[atkChoice].name + ' grows ' + friendlyPk.name + ' attack by ' + str(dmg) + '\n')
                
                elif friendlyPk.moves[atkChoice].purpose == 'DEF_Buff':
                    dmg = abs(friendlyPk.moves[atkChoice].generateDamage())
                    friendlyPk.DfBuff(dmg)
                    delayPrint(friendlyPk.moves[atkChoice].name + ' grows ' + friendlyPk.name + ' defence by ' + str(dmg) + '\n')

                elif friendlyPk.moves[atkChoice].purpose == 'SATK_Buff':
                    dmg = abs(friendlyPk.moves[atkChoice].generateDamage())
                    friendlyPk.SAtkBuff(dmg)
                    delayPrint(friendlyPk.moves[atkChoice].name + ' grows ' + friendlyPk.name + ' special attack by ' + str(dmg) + '\n')
                
                elif friendlyPk.moves[atkChoice].purpose == 'SDEF_Buff':
                    dmg = abs(friendlyPk.moves[atkChoice].generateDamage())
                    friendlyPk.SDfBuff(dmg)
                    delayPrint(friendlyPk.moves[atkChoice].name + ' grows ' + friendlyPk.name + ' special defence by ' + str(dmg) + '\n')

                elif friendlyPk.moves[atkChoice].purpose == 'SPD_Buff':
                    dmg = abs(friendlyPk.moves[atkChoice].generateDamage())
                    friendlyPk.SpeedBuff(dmg)
                    delayPrint(friendlyPk.moves[atkChoice].name + ' grows ' + friendlyPk.name + ' speed by ' + str(dmg) + '\n')

            else:
                adventage = friendlyPk.moves[atkChoice].isDominant(Player2.pokemonQuantity[enemy])
                dmg = friendlyPk.moves[atkChoice].generateDamage()
                Player2.pokemonQuantity[enemy].takeDamageSpecial(dmg, adventage)
                
                if adventage == True:
                    delayPrint(friendlyPk.moves[atkChoice].name + ' was super effective !' + '\n')
                else:
                    delayPrint(friendlyPk.moves[atkChoice].name + ' was not very effective against '+ Player2.pokemonQuantity[enemy].name + '\n')
            
            # Jesli padl to usuwany jest 
            if Player2.pokemonQuantity[enemy].getHp() == 0:
                print(Player2.pokemonQuantity[enemy].name.replace(" ", "") + ' has died.')
                del Player2.pokemonQuantity[enemy]        
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
    # wypisanie stanu LP    
    print(bcolors.BOLD + "Enemy's Pk:" + bcolors.ENDC)
    for enemyPk in Player2.pokemonQuantity:
        enemyPk.printHp()

    for foe in Player2.pokemonQuantity:
        if Player1.pokemonQuantity == []:
            endMesssage(Player2)
        #wybor akcji
        foe.ChooseAction()
        choice = int(input())
        
        # wypisanie atakow
        if choice == 1:
            friendo = foe.chooseTarget(Player1.pokemonQuantity)
            foe.ChooseAttack()
            atkChoice = int(input()) - 1
            
            if foe.moves[atkChoice].type == NORMAL:
                
                if foe.moves[atkChoice].purpose == 'damageDeal':
                    dmg = abs(foe.moves[atkChoice].generateDamage())
                    Player1.pokemonQuantity[friendo].takeDamageNormal(dmg)
                    delayPrint(foe.moves[atkChoice].name + ' deals '+ str(dmg) + ' damage to ' + Player1.pokemonQuantity[friendo].name + '\n')
                
                elif foe.moves[atkChoice].purpose == 'ATK_debuff':
                    dmg = abs(foe.moves[atkChoice].generateDamage())
                    Player1.pokemonQuantity[friendo].getAtkDebuff(dmg)
                    delayPrint(foe.moves[atkChoice].name + ' decreased attack of ' + Player1.pokemonQuantity[friendo].name + ' by ' + str(dmg) + '\n')
                
                elif foe.moves[atkChoice].purpose == 'DEF_debuff':
                    dmg = abs(foe.moves[atkChoice].generateDamage())
                    Player1.pokemonQuantity[friendo].getDefDebuff(dmg)
                    delayPrint(foe.moves[atkChoice].name + ' decreased defence of ' + Player1.pokemonQuantity[friendo].name + ' by ' + str(dmg) + '\n')
                
                elif foe.moves[atkChoice].purpose == 'SPD_debuff':
                    dmg = abs(foe.moves[atkChoice].generateDamage())
                    Player1.pokemonQuantity[friendo].getSpeedDebuff(dmg)
                    delayPrint(foe.moves[atkChoice].name + ' decreased speeed of ' + Player1.pokemonQuantity[friendo].name + ' by ' + str(dmg) + '\n')
                
                elif foe.moves[atkChoice].purpose == 'SATK_debuff':
                    dmg = abs(foe.moves[atkChoice].generateDamage())
                    Player1.pokemonQuantity[friendo].getSattackDebuff(dmg)
                    delayPrint(foe.moves[atkChoice].name + ' decreased special attack of ' + Player1.pokemonQuantity[friendo].name + ' by ' + str(dmg) + '\n')
                
                elif foe.moves[atkChoice].purpose == 'SDEF_debuff':
                    dmg = abs(foe.moves[atkChoice].generateDamage())
                    Player1.pokemonQuantity[friendo].getSdfDebuff(dmg)
                    delayPrint(foe.moves[atkChoice].name + ' decreased special defence of ' + Player1.pokemonQuantity[friendo].name + ' by ' + str(dmg) + '\n')
                
                elif foe.moves[atkChoice].purpose == 'HealUp':
                    dmg = abs(foe.moves[atkChoice].generateDamage())
                    foe.heal(dmg)
                    delayPrint(foe.moves[atkChoice].name + ' heals ' + foe.name + ' by ' + str(dmg) + '\n')
            
            else:
                adventage = foe.moves[atkChoice].isDominant(foe)
                dmg = foe.moves[atkChoice].generateDamage()
                Player1.pokemonQuantity[friendo].takeDamageSpecial(dmg, adventage)
                
                if adventage == True:
                    delayPrint(foe.moves[atkChoice].name + ' was super effective !' + '\n')
                else:
                    delayPrint(foe.moves[atkChoice].name + ' was not very effective against '+ Player1.pokemonQuantity[friendo].name + '\n')
                    
            if Player1.pokemonQuantity[friendo].getHp() == 0:
                print(Player1.pokemonQuantity[friendo].name.replace(" ", "") + ' has died.')
                del Player1.pokemonQuantity[friendo]

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
    
    #Sprawdzenie czy sie wygralo czy przegralo
    defeatedEnemy = 0
    for foe in Player2.pokemonQuantity:
        if foe.getHp() == 0:
            defeatedEnemy += 1

    defeatedPk = 0
    for poke in Player1.pokemonQuantity:
        if poke.getHp() == 0:
            defeatedPk += 1
        
    if defeatedEnemy  == 2:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        run = False
        
    elif defeatedPk == 2:
        print(bcolors.OKRED + "YOU DIED :(" + bcolors.ENDC)
        run = False
