from classes.colors import bcolors

class Player:
    def __init__(self, name, pokemonQuantity, items):
        self.name = name
        self.pokemonQuantity = pokemonQuantity
        self.items = items
    
    def chooseItem(self):
        i = 1
        print('\n' + bcolors.OKGREEN + bcolors.BOLD + "ITEMS: " + bcolors.ENDC)
        for item in self.items:
            print("    " + str(i) + ".", item["item"].name, " : ", item["item"].description + " (x" + str(item["quantity"]) + ")")
            i += 1
