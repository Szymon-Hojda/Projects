import random

def dice_roll():
    random_throw = random.randint(1,6)

    if random_throw == 1:
        print('.-----------.')
        print('|           |')
        print('|     0     |')
        print('|           |')
        print('`-----------`')
    if random_throw == 2:
        print('.-----------.')
        print('|           |')
        print('|   0   0   |')
        print('|           |')
        print('`-----------`')
    if random_throw == 3:
        print('.-----------.')
        print('|     0     |')
        print('|     0     |')
        print('|     0     |')
        print('`-----------`')
    if random_throw == 4:
        print('.-----------.')
        print('|   0   0   |')
        print('|           |')
        print('|   0   0   |')
        print('`-----------`')
    if random_throw == 5:
        print('.-----------.')
        print('|   0   0   |')
        print('|     0     |')
        print('|   0   0   |')
        print('`-----------`')
    if random_throw == 6:
        print('.-----------.')
        print('|   0   0   |')
        print('|   0   0   |')
        print('|   0   0   |')
        print('`-----------`')

print('---This is simulator of Dice roll---')
dice_roll()

while True:
    UserInput = input("Press y to roll again : \n")
    if UserInput == 'y':
        dice_roll()y
    else:
        break