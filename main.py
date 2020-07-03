import sys
import time
import secrets
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

def GiveAway(list):
    p1List = []
    p2List = []
    choice1 = secrets.choice(list)
    choice2 = secrets.choice(list)
    if choice1 != choice2:
        p1List.append(choice1)
        p2List.append(choice2)
    else:
        GiveAway(list)
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
poke5 = Pokemon(Rick, ELECTRIC, 20, 1, 5, 17, 17, 4, [ThunderBolt, Flamethrower, ThunderPunch, Recovery])

Morty = bcolors.OKBLUE + 'Morty' + bcolors.ENDC
poke6 = Pokemon(Morty, WATER, 19, 12, 10, 1, 5, 8, [VineWhip, LeafPunch, RazorLeaf, Recovery])

PokemonList = [poke1, poke2, poke3, poke4, poke5, poke6]

# Player's Pk
YoursPk, EnemysPk = GiveAway(PokemonList)
 

# Player's n stuff
strPlayer1 = bcolors.OKRED + 'Ash' + bcolors.ENDC
Player1 = Player(strPlayer1, YoursPk, Player1Set)

strPlayer2 = bcolors.OKBLUE + 'Gary' + bcolors.ENDC
Player2 = Player(strPlayer2, EnemysPk, Player2Set)

delayPrint(Player2.name + ' wants to fight!')

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
        choice = int(input('Choose action: '))
        
        # wypisanie atakow
        if choice == 1:

            enemy = friendlyPk.chooseTarget(Player2.pokemonQuantity)
            friendlyPk.ChooseAttack()
            atkChoice = int(input('        Choose attack:')) - 1

            move = friendlyPk.moves[atkChoice]

            if move.type == NORMAL:
                
                if move.purpose == 'damageDeal':
                    dmg = abs(move.getDamageValue())
                    damage = friendlyPk.generateDamage(dmg)
                    Player2.pokemonQuantity[enemy].takeDamageNormal(damage)
                    delayPrint(move.name + ' deals '+ str(damage - Player2.pokemonQuantity[enemy].getDf()) + ' damage to ' + Player2.pokemonQuantity[enemy].name + '\n')
                
                elif move.purpose == 'ATK_debuff':
                    dmg = abs(move.generateBuffDamage())
                    Player2.pokemonQuantity[enemy].getAtkDebuff(dmg)
                    delayPrint(move.name + ' decreased attack of ' + Player2.pokemonQuantity[enemy].name + ' by ' + str(dmg) + '\n')
                
                elif move.purpose == 'DEF_debuff':
                    dmg = abs(move.generateBuffDamage())
                    Player2.pokemonQuantity[enemy].getDefDebuff(dmg)
                    delayPrint(move.name + ' decreased defence of ' + Player2.pokemonQuantity[enemy].name + ' by ' + str(dmg) + '\n')
                
                elif move.purpose == 'SPD_debuff':
                    dmg = abs(move.generateBuffDamage())
                    Player2.pokemonQuantity[enemy].getSpeedDebuff(dmg)
                    delayPrint(move.name + ' decreased speeed of ' + Player2.pokemonQuantity[enemy].name + ' by ' + str(dmg) + '\n')
                
                elif move.purpose == 'SATK_debuff':
                    dmg = abs(move.generateBuffDamage())
                    Player2.pokemonQuantity[enemy].getSattackDebuff(dmg)
                    delayPrint(move.name + ' decreased special attack of ' + Player2.pokemonQuantity[enemy].name + ' by ' + str(dmg) + '\n')
                
                elif move.purpose == 'SDEF_debuff':
                    dmg = abs(move.generateBuffDamage())
                    Player2.pokemonQuantity[enemy].getSdfDebuff(dmg)
                    delayPrint(move.name + ' decreased special defence of ' + Player2.pokemonQuantity[enemy].name + ' by ' + str(dmg) + '\n')
                
                elif move.purpose == 'HealUp':
                    dmg = abs(move.generateBuffDamage())
                    friendlyPk.heal(dmg)
                    delayPrint(move.name + ' heals ' + friendlyPk.name + ' by ' + str(dmg) + '\n')
                
                # Buffs
                elif move.purpose == 'ATK_Buff':
                    dmg = abs(move.generateBuffDamage())
                    friendlyPk.AtkBuff(dmg)
                    delayPrint(move.name + ' grows ' + friendlyPk.name + ' attack by ' + str(dmg) + '\n')
                
                elif move.purpose == 'DEF_Buff':
                    dmg = abs(move.generateBuffDamage())
                    friendlyPk.DfBuff(dmg)
                    delayPrint(move.name + ' grows ' + friendlyPk.name + ' defence by ' + str(dmg) + '\n')

                elif move.purpose == 'SATK_Buff':
                    dmg = abs(move.generateBuffDamage())
                    friendlyPk.SAtkBuff(dmg)
                    delayPrint(move.name + ' grows ' + friendlyPk.name + ' special attack by ' + str(dmg) + '\n')
                
                elif move.purpose == 'SDEF_Buff':
                    dmg = abs(move.generateBuffDamage())
                    friendlyPk.SDfBuff(dmg)
                    delayPrint(move.name + ' grows ' + friendlyPk.name + ' special defence by ' + str(dmg) + '\n')

                elif move.purpose == 'SPD_Buff':
                    dmg = abs(move.generateBuffDamage())
                    friendlyPk.SpeedBuff(dmg)
                    delayPrint(move.name + ' grows ' + friendlyPk.name + ' speed by ' + str(dmg) + '\n')
            
            # Ataki oparte na typie np ogniu
            else:
                adventage = move.isDominant(Player2.pokemonQuantity[enemy])
                dmg = move.generateDamage()
                damage = friendlyPk.generateDamageSpecial(dmg)
                Player2.pokemonQuantity[enemy].takeDamageSpecial(damage, adventage)
                
                if adventage == True:
                    print(move.name + ' deals ' + str(int(damage * 2.5 - Player2.pokemonQuantity[enemy].getSdf())) + '\n')
                    delayPrint('It was super effective !' + '\n')
                else:
                    print(move.name + ' deals ' + str(int(damage - Player2.pokemonQuantity[enemy].getSdf())) + '\n')
                    delayPrint('It was not very effective against '+ Player2.pokemonQuantity[enemy].name + '\n')
            
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
        choice = int(input('Choose action: '))
        
        # wypisanie atakow
        if choice == 1:
            friendo = foe.chooseTarget(Player1.pokemonQuantity)
            foe.ChooseAttack()
            atkChoice = int(input('        Choose attack: ')) - 1
            
            move = foe.moves[atkChoice]

            if move.type == NORMAL:

                if move.purpose == 'damageDeal':
                    dmg = abs(move.getDamageValue())
                    damage = foe.generateNormalDamage(dmg)
                    Player1.pokemonQuantity[friendo].takeDamageNormal(damage)
                    delayPrint(move.name + ' deals '+ str(damage - Player1.pokemonQuantity[friendo].getDf()) + ' damage to ' + Player1.pokemonQuantity[friendo].name + '\n')
                
                elif move.purpose == 'ATK_debuff':
                    dmg = abs(move.generateBuffDamage())
                    Player1.pokemonQuantity[friendo].getAtkDebuff(dmg)
                    delayPrint(move.name + ' decreased attack of ' + Player1.pokemonQuantity[friendo].name + ' by ' + str(dmg) + '\n')
                
                elif move.purpose == 'DEF_debuff':
                    dmg = abs(move.generateBuffDamage())
                    Player1.pokemonQuantity[friendo].getDefDebuff(dmg)
                    delayPrint(move.name + ' decreased defence of ' + Player1.pokemonQuantity[friendo].name + ' by ' + str(dmg) + '\n')
                
                elif move.purpose == 'SPD_debuff':
                    dmg = abs(move.generateBuffDamage())
                    Player1.pokemonQuantity[friendo].getSpeedDebuff(dmg)
                    delayPrint(move.name + ' decreased speeed of ' + Player1.pokemonQuantity[friendo].name + ' by ' + str(dmg) + '\n')
                
                elif move.purpose == 'SATK_debuff':
                    dmg = abs(move.generateBuffDamage())
                    Player1.pokemonQuantity[friendo].getSattackDebuff(dmg)
                    delayPrint(move.name + ' decreased special attack of ' + Player1.pokemonQuantity[friendo].name + ' by ' + str(dmg) + '\n')
                
                elif move.purpose == 'SDEF_debuff':
                    dmg = abs(move.generateBuffDamage())
                    Player1.pokemonQuantity[friendo].getSdfDebuff(dmg)
                    delayPrint(move.name + ' decreased special defence of ' + Player1.pokemonQuantity[friendo].name + ' by ' + str(dmg) + '\n')
                
                elif move.purpose == 'HealUp':
                    dmg = abs(move.generateBuffDamage())
                    foe.heal(dmg)
                    delayPrint(move.name + ' heals ' + foe.name + ' by ' + str(dmg) + '\n')

                # Buffs
                elif move.purpose == 'ATK_Buff':
                    dmg = abs(move.generateBuffDamage())
                    foe.AtkBuff(dmg)
                    delayPrint(move.name + ' grows ' + foe.name + ' attack by ' + str(dmg) + '\n')
                
                elif move.purpose == 'DEF_Buff':
                    dmg = abs(move.generateBuffDamage())
                    foe.DfBuff(dmg)
                    delayPrint(move.name + ' grows ' + foe.name + ' defence by ' + str(dmg) + '\n')

                elif move.purpose == 'SATK_Buff':
                    dmg = abs(move.generateBuffDamage())
                    foe.SAtkBuff(dmg)
                    delayPrint(move.name + ' grows ' + foe.name + ' special attack by ' + str(dmg) + '\n')
                
                elif move.purpose == 'SDEF_Buff':
                    dmg = abs(move.generateBuffDamage())
                    foe.SDfBuff(dmg)
                    delayPrint(move.name + ' grows ' + foe.name + ' special defence by ' + str(dmg) + '\n')

                elif move.purpose == 'SPD_Buff':
                    dmg = abs(move.generateBuffDamage())
                    foe.SpeedBuff(dmg)
                    delayPrint(move.name + ' grows ' + foe.name + ' speed by ' + str(dmg) + '\n')
            
            else:
                adventage = move.isDominant(foe)
                dmg = move.generateDamage()
                damage = foe.generateDamageSpecial(dmg)
                Player1.pokemonQuantity[friendo].takeDamageSpecial(damage, adventage)
                
                if adventage == True:
                    delayPrint(move.name + ' deals ' + str(int(damage *2.5 - Player1.pokemonQuantity[friendo].getSdf())))
                    delayPrint('It was super effective !' + '\n')
                else:
                    delayPrint('It was not very effective against '+ Player1.pokemonQuantity[friendo].name + '\n')
                    
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
