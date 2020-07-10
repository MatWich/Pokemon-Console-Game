import sys
from classes.colors import bcolors
from classes.pokemon import Pokemon
from classes.moves import Moves 

class Player:
    def __init__(self, name, money, pokemonQuantity, items):
        self.name = name
        self.money = money
        self.pokemonQuantity = pokemonQuantity
        self.items = items

    def getPokemonQuantity(self):
        return self.pokemonQuantity

    # UI

    def choosePokemon(self):
        i = 1
        print(bcolors.OKGREEN + bcolors.BOLD + "    " + self.name + " Pokemons" + bcolors.ENDC)
        for Pk in self.pokemonQuantity:
            print("    " + str(i) + ".", Pk.name)
            i += 1
        choice = int(input('Choose PoKemon: ')) - 1
        return choice

    def chooseItem(self):
        i = 1
        print('\n' + bcolors.OKGREEN + bcolors.BOLD + "ITEMS: " + bcolors.ENDC)
        for item in self.items:
            print("    " + str(i) + ".", item["item"].name, " : ", item["item"].description + " (x" + str(item["quantity"]) + ")")
            i += 1
        choice = int(input('Choose item: ')) - 1
        return choice

    def MoneyLoss(self, Player):
        moneyLost = self.money // 3
            
        self.money -= moneyLost
        if self.money < 0:
            self.money = 0

        Player.money += moneyLost
        print(Player.name + ' got ' + str(moneyLost) + '$ from ' + self.name)
        return self.money

    # End game function
    def endMesssage(self, Player):
        print(Player.name + ' has won a fight!')
        sys.exit(0)

    # Sprawdza czy jest jeszcze z kim walczyc
    def Lose(self, Player):
        if self.getPokemonQuantity() == []:
            self.MoneyLoss(Player)
            self.endMesssage(Player)

    def PokemonDamageCalculation(self, Player, current, enemy, atkChoice):
        self.Lose(Player)
        Pokemon1 = self.pokemonQuantity[current]    # Zadaje obrazenia
        Pokemon2 = Player.pokemonQuantity[enemy]    # Zbiera bęcki

        if Pokemon1.moves[atkChoice]["sp"] == 0:
            print(bcolors.BLINK + 'No SP left ... ' + bcolors.ENDC)
            atkChoice = Pokemon1.ChooseAttack()
            self.PokemonDamageCalculation(Player, current, enemy, atkChoice)
        else:
            Pokemon1.moves[atkChoice]["sp"] -= 1

        move = Pokemon1.moves[atkChoice]["move"]    # trzeba w mainie wybrac atak i pozostale rzeczy dalej

        # Normal attacks
        if move.purpose == 'damageDeal':
            dmg = abs(move.getDamageValue())
            damage = Pokemon1.generateDamage(dmg)
            Pokemon2.takeDamageNormal(damage)
            print(move.name + ' deals ' + str(int(damage - Pokemon2.getDf())) + ' damage to', Pokemon2.name + '\n')
        
        # Debuffs
        elif move.purpose == 'ATK_Debuff':
            dmg = abs(move.getDamageValue())
            Pokemon2.getAtkDebuff(dmg)
            print(move.name + ' decreased attack of '+ Pokemon2.name + ' by ' + str(dmg) + '\n') 

        elif (move.purpose == 'DEF_Debuff'):
            dmg = abs(move.getDamageValue())
            Pokemon2.getDefDebuff(dmg)
            print(move.name + ' decreased defence of '+ Pokemon2.name + ' by ' + str(dmg) + '\n') 

        elif move.purpose == 'SATK_Debuff':
            dmg = abs(move.getDamageValue())
            Pokemon2.getSAtkDebuff(dmg)
            print(move.name + ' decreased special attack of '+ Pokemon2.name + ' by ' + str(dmg) + '\n')

        elif move.purpose == 'SDEF_Debuff':
            dmg = abs(move.getDamageValue())
            Pokemon2.getAtkDebuff(dmg)
            print(move.name + ' decreased special defence of '+ Pokemon2.name + ' by ' + str(dmg) + '\n')  

        elif move.purpose == 'SPD_Debuff':
            dmg = abs(move.getDamageValue())
            Pokemon2.getSpeedDebuff(dmg)
            print(move.name + ' decreased speed of '+ Pokemon2.name + ' by ' + str(dmg) + '\n')

        # Heal
        elif move.purpose == 'HealUp':
            dmg = abs(move.getDamageValue())
            Pokemon2.getAtkDebuff(dmg)
            print(move.name + ' heals  '+ Pokemon1.name + ' by ' + str(dmg) + '\n') 

        # Buffs
        elif move.purpose == 'ATK_Buff':
            dmg = abs(move.generateBuffDamage())
            Pokemon1.AtkBuff(dmg)
            print(move.name + ' grows ' + Pokemon1.name + ' attack by ' + str(dmg) +'\n')

        elif move.purpose == 'DEF_Buff':
            dmg = abs(move.generateBuffDamage())
            Pokemon1.DefBuff(dmg)
            print(move.name + ' grows ' + Pokemon1.name + ' defence by ' + str(dmg) +'\n')

        elif move.purpose == 'SATK_Buff':
            dmg = abs(move.generateBuffDamage())
            Pokemon1.SAtkBuff(dmg)
            print(move.name + ' grows ' + Pokemon1.name + ' special attack by ' + str(dmg) +'\n')

        elif move.purpose == 'SDEF_Buff':
            dmg = abs(move.generateBuffDamage())
            Pokemon1.SDefBuff(dmg)
            print(move.name + ' grows ' + Pokemon1.name + ' special defence by ' + str(dmg) +'\n')
        
        elif move.purpose == 'SPD_Buff':
            dmg = abs(move.generateBuffDamage())
            Pokemon1.SpeedBuff(dmg)
            print(move.name + ' grows ' + Pokemon1.name + ' attack by ' + str(dmg) +'\n')
    
        # Atribute Attacks
        else:
            advantage = move.isDominant(Pokemon2)           # sprawdza czy podatny
            mult = move.generateDamageMult()                # sprawdza przelicznik
            damage = Pokemon1.generateDamageSpecial(mult)   # generuje obrazenia zadane przez atak Pokemon1
            Pokemon2.takeDamageSpecial(damage, advantage)
            # Wypisanie issue with proper number
            if advantage == True:
                print(move.name + ' deals ' + str(int(2.5 * damage - Pokemon2.getSDf())) + ' to ' + Pokemon2.name + '\n')
                print('It was super effective!' + '\n')
            else:
                print(move.name + ' deals' + str(int(damage - Pokemon2.getSDf())) + ' to ' + Pokemon2.name + '\n')
                print('It was not very effective...')
    
        # Remove fainted Pokemon
        if Pokemon2.Fainted() ==  True:
            del Player.pokemonQuantity[enemy]
        return self, Player
        
    def ItemDamageCalculation(self, Player):
        self.Lose(Player)

        itemChoice = self.chooseItem()

        item = self.items[itemChoice]["item"]

        if self.items[itemChoice]["quantity"] == 0:
            print(bcolors.BLINK + 'None of that left :(' + bcolors.ENDC + '\n')
            self.ItemDamageCalculation(Player)        # zamiast continue nwm czy dziala XD
        else:
            self.items[itemChoice]["quantity"] -= 1
        
        if item.type == "potion":
            # used to list pk
            i = 1
            for pk in self.pokemonQuantity:
                print(str(i) + '.')
                pk.printHp()
                i += 1
            pkChoice = int(input('Choose PoKemon to heal!')) - 1
            self.pokemonQuantity[pkChoice].heal(item.prop)
            print(bcolors.OKGREEN + item.name + ' heals for ' + str(item.prop) + ' Hp ' + self.pokemonQuantity[pkChoice].name + bcolors.ENDC)
        
        elif item.type == "weapon":
            i = 1
            for pk in Player.pokemonQuantity:
                print(str(i) + '. ')
                pk.printHp()
                i += 1
            pkChoice = int(input('Choose Pokemon to deal damage to it!')) - 1
            Player.pokemonQuantity[pkChoice].takeDamageNormal(item.prop)
            print(bcolors.OKRED + item.name + ' deals ' + str(item.prop) + ' damage to ' + Player.pokemonQuantity[pkChoice].name + bcolors.ENDC)
        
        # Remove fainted Pokemon
        for pk in Player.pokemonQuantity:
            if pk.Fainted() == True:
                del Player.pokemonQuantity[pkChoice]
        
        return self, Player


