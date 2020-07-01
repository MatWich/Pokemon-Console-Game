from classes.colors import bcolors
from classes.colors import WATER, FIRE, GRASS, ROCK, ELECTRIC, NORMAL
from classes.pokemon import Pokemon
from classes.moves import Moves

# MOVES
Flamethrower = Moves("FlameThrower", 50, FIRE, 'damageDeal')
FirePunch = Moves("Fire Punch", 35, FIRE, 'damageDeal')
Recovery = Moves("Recovery", 80, NORMAL, 'HealUp')
Growl = Moves("Growl", 2, NORMAL, 'ATK_Debuff')
# Pokemon
bigHungus = bcolors.OKBLUE + 'Big Hungus' + bcolors.ENDC
poke = Pokemon(bigHungus, WATER, 200, 23, 2, 2, 100, 2, [Flamethrower, FirePunch, Recovery, Growl])

print('Poczatkowe Hp: ', poke.getHp())
dmg = Flamethrower.generateDamage()

czyMaPrzewage = Flamethrower.isDominant(poke)

poke.takeDamageSpecial(dmg, czyMaPrzewage)
print('Hp po przyjeciu obrazen', poke.getHp())

ileHp = Recovery.generateDamage()
print('Wygenerowana ilosc zdrowia do przywrocenia: ', ileHp)
poke.heal(ileHp)
print('Hp po wyleczeniu', poke.getHp())


'''
#MainLoop
run = True
while run:
    pass
'''