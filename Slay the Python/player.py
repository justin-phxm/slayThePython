import random
class Player:
    #STATS
    def __init__(self, health=20, attack=5, defense=0):
        self.health = health
        self.attack = attack
        self.defense = defense

    def get_data(self):
        print(f'Health: {self.health}\nAttack: {self.attack}\nDefense: {self.defense}')

    def default_stats(self):
        self.attack = 5
        self.defense = 0

    def player_choice(self):
        user_choice = input('It is your turn: \n1. Attack\n2. defend\n3. Buff\n4. Appraise\nEnter choice: ')
        return user_choice