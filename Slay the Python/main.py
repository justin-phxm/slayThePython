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
                user.attack = user.attack * 3

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
enemy1 = asset_database.Battie()

print('''Hello player... this is a game I am too tired to finish...
Unfortunately, Python is not as easy as I thought.
Creating assets were the easy part, creating an interesting combat system is not.
I wanted to give all the enemies in this game certain traits, such as
Infinitely stacking damage
Block counters
Baby spawns
multiple target fights
I have run out of creative ideas.
Maybe I will return when I have more knowledge.
Until next time.
 ''')



print('''You wake in darkness. Your head is pulsing in pain.
A water droplet hits you on the forehead and you can feel it splatter across your face.
"Where am I?", you whisper to yourself.

The surface below you is soft, warm, and smells of leather.
Feeling around the smooth surface with your hands, you realize it's a bed.
All of a sudden, the room bursts with light. Flames surround you and you feel the heat biting at your skin.

 ''')
###BATTIE FIGHT###
enemy1.greet()
enemy1.img()
print('A wild Battie has appeared!')
print()

combat()

###Louse Fight###

enemy1 = asset_database.Louse()
enemy1.img()
enemy1.greet()
print('A louse sneaks up from behind you, sniffing your behind...')

combat()

###Nemesis Fight###


enemy1 = asset_database.Nemesis()
print('''
STOMP*STOMP*STOMP* 
You feel a cold chill crawl down your spine. 
The floor shakes as you hear a thunder slowly approach you.
Koopa Troopa (Temp name) appears. ''')
enemy1.img()
enemy1.greet()

combat()

##Double Enemy Fight###
enemy1 = asset_database.Lagavulin()
enemy1.img()
enemy1.greet()

print('The Lagavulin makes scary noises and you are scared, losing strength.')

combat()

