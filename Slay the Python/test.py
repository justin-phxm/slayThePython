#Combat system
import asset_database
import player
import time
import random

def combat():
    buff = False
    while enemy1.health > 0:
        user.default_stats()
        ####User Turn####
        player_choice = user.player_choice()
        if player_choice == '1':
            if buff == True:
                user.attack = user.attack * 2

            enemy1.health = enemy1.health - (user.attack - enemy1.defense)
            print(f'You have attacked for {user.attack} damage!')
            print(f'The {enemy1.name()} has {enemy1.health} health remaining.')
            print()

        if player_choice == '2':
            print('Bracing yourself, you take a defensive position.')
            user.defense += 1

        if player_choice == '3':
            print('You pump yourself up, taking an offensive position.')
            buff = True

        if player_choice == '4':
            print(f'''
___ENEMY INFO___
Health: {enemy1.health}
Attack: {enemy1.attack}
Defense: {enemy1.defense}
''')

        ####Enemy Turn####
        if enemy1.health > 0:
            user.health = user.health - (enemy1.attack - user.defense)
            print(f'The {enemy1.name()} has attacked you for {enemy1.attack - user.defense} damage!')
            print()
            pass

        if user.health <= 0:
            print('You died')
            quit()           
        else:
            print(f'You have {user.health} health remaining!')

    print(f'Congratulations! You have defeated the {enemy1.name()}.')


###MAIN####
user = player.Player()

enemy1 = asset_database.Lagavulin()
enemy1.img()
enemy1.greet()

print('The Lagavulin makes scary noises and you are scared, losing strength.')

combat()
if enemy1.name() == 'Lagavulin':
    print('ERROR' * 80)