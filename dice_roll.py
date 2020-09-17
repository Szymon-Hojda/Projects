import random

#print(random_throw)
print('This is a dice stimulator\n')

def rzut_kostki():
    random_throw = random.randint(1,6)
    ###############1###############
    if random_throw == 1:
        for i in range(5):
            if i == 0:
                print('.-----------.')
            elif i == 4:
                print('`-----------`')
            elif i == 2:
                print('|     ' + '0' +'     |')

            else:
                print('|           |')
    ###############2###############
    if random_throw == 2:
        for i in range(5):
            if i == 0:
                print('.-----------.')
            elif i == 4:
                print('`-----------`')
            elif i == 2:
                print('|   0   0   |')

            else:
                print('|           |')
    ###############3###############
    if random_throw == 3:
        for i in range(5):
            if i == 0:
                print('.-----------.')
            elif i == 4:
                print('`-----------`')
            elif i == 2:
                print('|     ' + '0' +'     |')

            else:
                print('|     0     |')
    ###############4###############
    if random_throw == 4:
        for i in range(5):
            if i == 0:
                print('.-----------.')
            elif i == 4:
                print('`-----------`')
            elif i == 2:
                print('|     ' + '' +'      |')
            elif i == 1 or i == 3:
                print('|  0     0  |')
    ###############5###############
    if random_throw == 5:
        for i in range(5):
            if i == 0:
                print('.-----------.')
            elif i == 4:
                print('`-----------`')
            elif i == 2:
                print('|     ' + '0' +'     |')


            elif i == 1 or i == 3:

                print('|  0     0  |')
    ###############6###############
    if random_throw == 6:
        for i in range(5):
            if i == 0:
                print('.-----------.')
            elif i == 4:
                print('`-----------`')
            elif i == 2:
                print('|     ' + '' +'      |')

            else:
                print('|  0  0  0  |')
rzut_kostki()
while True:
    UserInput = input("Press y to roll again.")
    if UserInput == 'y':
        rzut_kostki()
