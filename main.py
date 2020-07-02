import sys
import time
from classes.colors import bcolors
from classes.colors import WATER, FIRE, GRASS, ROCK, ELECTRIC, NORMAL
from classes.pokemon import Pokemon
from classes.moves import Moves

def delayPrint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

def endMesssage(Pokemon):
    delayPrint(Pokemon.name + ' has won a fight!')

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
ThunderPunch = Moves("Thunder Punch", 35, ELECTRIC, 'damageDeal')
#ROCK
strRockThrow = bcolors.OKGREY + "Rock Throw" + bcolors.ENDC
RockThrow = Moves(strRockThrow, 50, ROCK, 'damageDeal')
strAvalanche = bcolors.OKGREY + "Avalanche" + bcolors.ENDC
Avalanche = Moves(strAvalanche, 80, ROCK, 'damageDeal')
strDefenceCurl = bcolors.OKGREY + "Defence Curl" + bcolors.ENDC
DefenceCurl = Moves("Defence Curl", 5, ROCK, 'DEF_buff')
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

# Players layouts
YoursPk = [poke1, poke4]
EnemysPk = [poke2, poke3]

#MainLoop
run = True
while run:
    # PLAYER'S TURN 
    # wypisanie statystyk LP
    print(bcolors.BOLD + "Your's Pk:" + bcolors.ENDC)
    for poke in YoursPk:
        poke.printHp()
    print('\n')

    for friendlyPk in YoursPk:
        # wybranie akcji
        friendlyPk.ChooseAction()
        choice = int(input())
        
        # wypisanie atakow
        if choice == 1:
            enemy = friendlyPk.chooseTarget(EnemysPk)
            friendlyPk.ChooseAttack()
            atkChoice = int(input()) - 1
            if friendlyPk.moves[atkChoice].type == NORMAL:
                
                if friendlyPk.moves[atkChoice].purpose == 'damageDeal':
                    dmg = abs(friendlyPk.moves[atkChoice].generateDamage())
                    EnemysPk[enemy].takeDamageNormal(dmg)
                    delayPrint(friendlyPk.moves[atkChoice].name + ' deals '+ str(dmg) + ' damage to ' + EnemysPk[enemy].name + '\n')
                
                elif friendlyPk.moves[atkChoice].purpose == 'ATK_debuff':
                    dmg = abs(friendlyPk.moves[atkChoice].generateDamage())
                    EnemysPk[enemy].getAtkDebuff(dmg)
                    delayPrint(friendlyPk.moves[atkChoice].name + ' decreased attack of ' + EnemysPk[enemy].name + ' by ' + str(dmg) + '\n')
                
                elif friendlyPk.moves[atkChoice].purpose == 'DEF_debuff':
                    dmg = abs(friendlyPk.moves[atkChoice].generateDamage())
                    EnemysPk[enemy].getDefDebuff(dmg)
                    delayPrint(friendlyPk.moves[atkChoice].name + ' decreased defence of ' + EnemysPk[enemy].name + ' by ' + str(dmg) + '\n')
                
                elif friendlyPk.moves[atkChoice].purpose == 'SPD_debuff':
                    dmg = abs(friendlyPk.moves[atkChoice].generateDamage())
                    EnemysPk[enemy].getSpeedDebuff(dmg)
                    delayPrint(friendlyPk.moves[atkChoice].name + ' decreased speeed of ' + EnemysPk[enemy].name + ' by ' + str(dmg) + '\n')
                
                elif friendlyPk.moves[atkChoice].purpose == 'SATK_debuff':
                    dmg = abs(friendlyPk.moves[atkChoice].generateDamage())
                    EnemysPk[enemy].getSattackDebuff(dmg)
                    delayPrint(friendlyPk.moves[atkChoice].name + ' decreased special attack of ' + EnemysPk[enemy].name + ' by ' + str(dmg) + '\n')
                
                elif friendlyPk.moves[atkChoice].purpose == 'SDEF_debuff':
                    dmg = abs(friendlyPk.moves[atkChoice].generateDamage())
                    EnemysPk[enemy].getSdfDebuff(dmg)
                    delayPrint(friendlyPk.moves[atkChoice].name + ' decreased special defence of ' + EnemysPk[enemy].name + ' by ' + str(dmg) + '\n')
                
                elif friendlyPk.moves[atkChoice].purpose == 'HealUp':
                    dmg = abs(friendlyPk.moves[atkChoice].generateDamage())
                    friendlyPk.heal(dmg)
                    delayPrint(friendlyPk.moves[atkChoice].name + ' heals ' + friendlyPk.name + ' by ' + str(dmg) + '\n')
            
            else:
                adventage = friendlyPk.moves[atkChoice].isDominant(EnemysPk[enemy])
                dmg = friendlyPk.moves[atkChoice].generateDamage()
                EnemysPk[enemy].takeDamageSpecial(dmg, adventage)
                
                if adventage == True:
                    delayPrint(friendlyPk.moves[atkChoice].name + ' was super effective !' + '\n')
                else:
                    delayPrint(friendlyPk.moves[atkChoice].name + ' was not very effective against '+ EnemysPk[enemy].name + '\n')
                    

        elif choice == 2:
            #choosing items
            print('In progress...')
            continue
        
        elif choice == 3:
            print(bcolors.BOLD + 'YOU ESCAPED' + bcolors.ENDC)
            exit(0)
        
        else:
            print('There is no option ', choice)
            break

    # ENEMY's TURN    
    # wypisanie stanu LP    
    print(bcolors.BOLD + "Enemy's Pk:" + bcolors.ENDC)
    for enemyPk in EnemysPk:
        enemyPk.printHp()

    for foe in EnemysPk:
        #wybor akcji
        foe.ChooseAction()
        choice = int(input())
        
        # wypisanie atakow
        if choice == 1:
            friendo = foe.chooseTarget(YoursPk)
            foe.ChooseAttack()
            atkChoice = int(input()) - 1
            
            if foe.moves[atkChoice].type == NORMAL:
                
                if foe.moves[atkChoice].purpose == 'damageDeal':
                    dmg = abs(foe.moves[atkChoice].generateDamage())
                    YoursPk[friendo].takeDamageNormal(dmg)
                    delayPrint(foe.moves[atkChoice].name + ' deals '+ str(dmg) + ' damage to ' + YoursPk[friendo].name + '\n')
                
                elif foe.moves[atkChoice].purpose == 'ATK_debuff':
                    dmg = abs(foe.moves[atkChoice].generateDamage())
                    YoursPk[friendo].getAtkDebuff(dmg)
                    delayPrint(foe.moves[atkChoice].name + ' decreased attack of ' + YoursPk[friendo].name + ' by ' + str(dmg) + '\n')
                
                elif foe.moves[atkChoice].purpose == 'DEF_debuff':
                    dmg = abs(foe.moves[atkChoice].generateDamage())
                    YoursPk[friendo].getDefDebuff(dmg)
                    delayPrint(foe.moves[atkChoice].name + ' decreased defence of ' + YoursPk[friendo].name + ' by ' + str(dmg) + '\n')
                
                elif foe.moves[atkChoice].purpose == 'SPD_debuff':
                    dmg = abs(foe.moves[atkChoice].generateDamage())
                    YoursPk[friendo].getSpeedDebuff(dmg)
                    delayPrint(foe.moves[atkChoice].name + ' decreased speeed of ' + YoursPk[friendo].name + ' by ' + str(dmg) + '\n')
                
                elif foe.moves[atkChoice].purpose == 'SATK_debuff':
                    dmg = abs(foe.moves[atkChoice].generateDamage())
                    YoursPk[friendo].getSattackDebuff(dmg)
                    delayPrint(foe.moves[atkChoice].name + ' decreased special attack of ' + YoursPk[friendo].name + ' by ' + str(dmg) + '\n')
                
                elif foe.moves[atkChoice].purpose == 'SDEF_debuff':
                    dmg = abs(foe.moves[atkChoice].generateDamage())
                    YoursPk[friendo].getSdfDebuff(dmg)
                    delayPrint(foe.moves[atkChoice].name + ' decreased special defence of ' + YoursPk[friendo].name + ' by ' + str(dmg) + '\n')
                
                elif foe.moves[atkChoice].purpose == 'HealUp':
                    dmg = abs(foe.moves[atkChoice].generateDamage())
                    foe.heal(dmg)
                    delayPrint(foe.moves[atkChoice].name + ' heals ' + foe.name + ' by ' + str(dmg) + '\n')
            
            else:
                adventage = foe.moves[atkChoice].isDominant(foe)
                dmg = foe.moves[atkChoice].generateDamage()
                YoursPk[friendo].takeDamageSpecial(dmg, adventage)
                
                if adventage == True:
                    delayPrint(foe.moves[atkChoice].name + ' was super effective !' + '\n')
                else:
                    delayPrint(foe.moves[atkChoice].name + ' was not very effective against '+ YoursPk[friendo].name + '\n')
                    

        elif choice == 2:
            #choosing items
            print('In progress...')
            continue
        
        elif choice == 3:
            print(bcolors.BOLD + 'YOU ESCAPED' + bcolors.ENDC)
            exit(0)
        
        else:
            print('There is no option ', choice)
            break
    
    
    #Sprawdzenie czy sie wygralo czy przegralo
    defeatedEnemy = 0
    for enemy in EnemysPk:
        if enemy.getHp() == 0:
            defeatedEnemy += 1

    defeatedPk = 0
    for poke in YoursPk:
        if poke.getHp() == 0:
            defeatedPk += 1
    
    if defeatedEnemy  == 2:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        run = False
    
    elif defeatedPk == 2:
        print(bcolors.OKRED + "YOU DIED :(" + bcolors.ENDC)
        run = False
