import sys
import config
from classes.colors import bcolors
from classes.colors import WATER, FIRE, GRASS, ROCK, ELECTRIC, NORMAL
from classes.items import Item
from classes.pokemon import Pokemon
from classes.moves import Moves
from classes.player import Player

# Player's Pk
YoursPk, EnemysPk = config.GiveAway(config.PokemonList)
 
# Player's n stuff
strPlayer1 = bcolors.OKRED + 'Ash' + bcolors.ENDC
Player1 = Player(strPlayer1, 100, YoursPk, config.Player1Set)

strPlayer2 = bcolors.OKBLUE + 'Gary' + bcolors.ENDC
Player2 = Player(strPlayer2, 999, EnemysPk, config.Player2Set)

''' GAME STARTS '''
config.delayPrint(Player2.name + ' wants to fight!' + '\n')

# Chosing Pk that you want to fight for you
P1Pokemon= Player1.choosePokemon()
P2Pokemon = Player2.choosePokemon()
Pokemon1 = Player1.pokemonQuantity[P1Pokemon]
Pokemon2 = Player2.pokemonQuantity[P2Pokemon]

turn = 1
czyPoczatekWalki = 0    # 0 No 1 Yes
#MainLoop
run = True
while run:

    # Checking winning conditions
    Player1.Lose(Player2)
    Player2.Lose(Player1)

    # Checking PoKemon status
    if Pokemon1.getHp() == 0:
        print("Choose another Pokemon " + Player1.name + ": ")
        P1Pokemon = Player1.choosePokemon()
        Pokemon1 = Player1.pokemonQuantity[P1Pokemon]
        czyPoczatekWalki = 1
        turn = 0
    elif Pokemon2.getHp() == 0:
        print("Choose another Pokemon " + Player2.name + ": ")
        P2Pokemon = Player2.choosePokemon()
        Pokemon2 = Player2.pokemonQuantity[P2Pokemon]
        czyPoczatekWalki = 1
        turn = 1
    else:
        czyPoczatekWalki = 0

    
    if czyPoczatekWalki % 2 == 1:
        # Which PoKemon is faster
        if Pokemon1.getSpeed() > Pokemon2.getSpeed():
            turn = 0
            czyPoczatekWalki = 0
        elif Pokemon1.getSpeed() < Pokemon2.getSpeed():
            turn = 1
            czyPoczatekWalki = 0
        else:
            turn = random.randint(0, 1)
            czyPoczatekWalki = 0


    if turn % 2 == 0:
        ''' PLAYER1'S TURN '''
        turn += 1
        # wypisanie statystyk LP
        print('\n' + bcolors.BOLD + Player1.name +" Pks:" + bcolors.ENDC)
        Pokemon1.printHp()
        print('\n' + bcolors.BOLD + Player2.name +" Pks:" + bcolors.ENDC)
        Pokemon2.printHp()
        print('\n')

        # wybranie akcji
        choice = Pokemon1.ChooseAction()
            
        # wypisanie atakow
        if choice == 1:
            atkChoice = Pokemon1.ChooseAttack()
            Player1, Player2 = Player1.PokemonDamageCalculation(Player2, P1Pokemon, P2Pokemon, atkChoice)
        
        # ITEMS
        elif choice == 2:
            Player1.ItemDamageCalculation(Player2)    
            
        # RUN BERRY RUN
        elif choice == 3:
            print(bcolors.BOLD + Player1.name + bcolors.BOLD +' escaped' + bcolors.ENDC)
            exit(0)
            
        # NOPE!!!
        else:
            print('There is no option ', choice)
            break
    elif turn % 2 == 1:
        '''Player2's turn'''
        turn += 1
        # wypisanie stanu LP    
        print('\n' + bcolors.BOLD + Player1.name +" Pks:" + bcolors.ENDC)
        Pokemon1.printHp()
        print('\n' + bcolors.BOLD + Player2.name +" Pks:" + bcolors.ENDC)
        Pokemon2.printHp()
        print('\n')

        #wybor akcji
        choice = Pokemon2.ChooseAction()
            
        # wypisanie atakow
        if choice == 1:
            atkChoice = Pokemon2.ChooseAttack()
            Player2, Player1 = Player2.PokemonDamageCalculation(Player1, P2Pokemon, P1Pokemon, atkChoice)

        # ITEMS
        elif choice == 2:
            Player2.ItemDamageCalculation(Player1)
            
        # WHY WOULD YOU LIKE TO DO THAT?
        elif choice == 3:
            print(bcolors.BOLD + Player2.name + bcolors.BOLD + ' ESCAPED' + bcolors.ENDC)
            exit(0)
            
        # THERE IS NO ESTER EGG HERE
        else:
            print('There is no option ', choice)
            continue

    else:
        print('Error accured')
    # else statement not always works so im setting it here
    czyPoczatekWalki = 0
    
