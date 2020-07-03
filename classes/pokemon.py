from classes.colors import bcolors, WATER, FIRE, ELECTRIC, GRASS, ROCK, NORMAL
from classes.moves import Moves

class Pokemon:
    def __init__(self, name, type, hp, attack, df, Sattack,  Sdf,  speed, moves):
        self.name = name
        self.type = type
        self.hp = hp
        self.maxHp = hp
        self.attack = attack
        self.realAttack = attack
        self.Sattack = Sattack
        self.Sdf = Sdf
        self.df = df
        self.realDf = df
        self.speed = speed
        self.realSpeed = speed
        self.moves = moves

        self.actions = ["Attack", "Items", "Run Away"]

    #Zwracanie wartosci statystyk

    def getHp(self):
        return self.hp

    def getAttack(self):
        return self.attack

    def getSattack(self):
        return self.Sattack

    def getDf(self):
        return self.df
    
    def getSDf(self):
        return self.Sdf

    def getSpeed(self):
        return self.speed

    # UI

    def ChooseAction(self):
        i = 1
        print('What ' + self.name + ' should do?')
        for action in self.actions:
            print('    ' + str(i) + '.', action)
            i += 1
        

    def ChooseAttack(self):
        i = 1
        print('        Which attack should be choosen?')
        for move in self.moves:
            print('            '+ str(i) + '.', move.name)
            i += 1

    def chooseTarget(self, enemies):
        i = 1
        print(bcolors.OKRED + bcolors.BOLD + "    TAEGET:" + bcolors.ENDC)
        for enemy in enemies:
            if enemy.getHp() != 0:
                print("        " + str(i) + ".", enemy.name)
                i += 1
        choice = int(input('    Choose target:')) - 1
        return choice

    def printHp(self):
        hpBar = ""
        hpBarTicks = (self.hp / self.maxHp) * 100 / 4
        while hpBarTicks >= 0:
            hpBar += "█"
            hpBarTicks -= 1
        
        while len(hpBar) < 25:
            hpBar += " "
        
        hpString = str(self.hp) + "/" + str(self.maxHp)
        currentHP = ""
        if len(hpString) < 9:
            decreased = 9 -len(hpString)

            while decreased > 0:
                currentHP += " "
                decreased -= 1

            currentHP += hpString
        else:
            currentHP = hpString
        #print("NAME               HP")
        #print('                    --------------------------')
        print(bcolors.BOLD + self.name  +
            currentHP + '|' + bcolors.OKGREEN + hpBar + bcolors.ENDC + '|') 
            
    # Przyjmowanie obrazen

    def takeDamageNormal(self, dmg):
        reduce = int(self.df)
        damage = int(dmg - reduce)
        if reduce > damage:
            self.hp -= 1
        else:
            self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def takeDamageSpecial(self, dmg, dominant):
        if dominant == True:
            dmg *= 2.5
        
        reduce = int(self.Sdf)
        
        if reduce > dmg:
            self.hp -= 1
        else:
            damage = int(dmg - reduce)
            self.hp -= damage
        
        if self.hp < 0:
            self.hp = 0
        return self.hp

    #umiejetnosci wplywajace na statystyki np recovery, growl

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxHp:
            self.hp = self.maxHp
        return self.hp

    # DEBUFFS

    def getAtkDebuff(self, debuff):
        self.attack -= debuff
        if self.attack <= 0:
            self.attack = 1


    def getDefDebuff(self, debuff):
        self.df -= debuff
        if self.df <= 0:
            self.df = 0
    
    def getSattackDebuff(self, debuff):
        self.Sattack -= debuff
        if self.Sattack <= 10:
            self.Sattack = 10
    
    def getSdfDebuff(self, debuff):
        self.Sdf -= debuff
        if self.Sdf < 0:
            self.Sdf = 1

    def getSpeedDebuff(self, debuff):
        self.speed -= debuff
        if self.speed <= 1: 
            self.speed = 1
    
    # BUFFS

    def AtkBuff(self, buff):
        self.attack += buff

    def DefBuff(self, buff):
        self.df += buff

    def SAtkBuff(self, buff):
        self.Sattack += buff

    def SDefBuff(self, buff):
        self.Sdf += buff

    def SpeedBuff(self, buff):
        self.speed += buff
    
    # Zadawanie obrazen

    def generateDamage(self, multiplayer):
        return int(self.attack * multiplayer)
    
    def generateNormalDamage(self, dmg):
        return int(self.attack + dmg)

    def generateDamageSpecial(self, multiplayer):
        return int(self.Sattack * multiplayer)

    # STATUS

    def Fainted(self):
        if self.getHp() == 0:
            print(self.name.replace(" ", "") + ' has fainted')
            return True
        else:
            return False


    

    
    
        



    