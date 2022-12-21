import random

print('Quit the game')
user_input = 0
while user_input != '3':
    user_input = input('Please enter a number:')
    print('loading...')
    if user_input == '4':
        quit()