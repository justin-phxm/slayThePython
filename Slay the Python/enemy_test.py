import random
class Battie:
    '''The first and most basic enemy, the Battie.'''
    def __init__(self, health = 10, attack = 1, defense = 0):
        self.health = health
        self.attack = attack
        self.defense = defense

    def get_data(self):
        print(f'Health: {self.health}\nAttack: {self.attack}\nDefense: {self.defense}')

    def greet(self):
        print('SCREEE! ' * 7)
    
    def img(self):
        print(r"""
    
_________________               _________________
 ~-.              \  |\___/|  /              .-~
     ~-.           \ / o o \ /           .-~
        >           \\  W  //           <
       /             /~---~\             \
      /_            |       |            _\
         ~-.        |       |        .-~
            ;        \     /        i
           /___      /\   /\      ___\
                ~-. /  \_/  \ .-~
                   V         V
""")