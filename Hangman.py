import time
import random


def hangman():
    words = [
        'baby', 'door', 'banana',
        'finger', 'fence', 'big',
        'swimming', 'pool', 'sun', 'church'
        , 'boy', 'bag',
        'alligator', 'mouse', 'birthday',
        'winter', "beach", 'tree',
        'teacher', 'king', "telephone"]
    r_word = random.choice(words)  # Random word from words.
    chances = 10  # number of chances
    guesses = []
    hiden_word = ['_'] * len(r_word)

    def bad_or_good_choice():  # change chances -1 or show good letter
        user_input = input('Give me a letter: ')
        if user_input in guesses:
            print('You already check that letter!')
        guesses.append(user_input)
        if user_input not in r_word:
            nonlocal chances
            chances -= 1
        elif user_input in r_word:
            for index, letter in enumerate(r_word):
                if letter == user_input:
                    letter_index = [index]
                    for index in letter_index:
                        hiden_word[index] = user_input

    print('*' * 45)
    print('Try to guess the word in less than 10 attemps')
    print('*' * 45)

    while chances != 0:
        if ''.join(hiden_word) == r_word:
            print('You Win!!!')
            print('That word was!: ', r_word)
            again = input('If u want try again press Y: ')
            if again == 'Y' or 'y':
                hangman()
            else:
                break
        if chances == 10:
            print('')
            print('')
            print('')
            print('')
            print('')
            print(' '.join(hiden_word))
            print()
            bad_or_good_choice()
        if chances == 9:
            print('._________.')
            print('|')
            print('|')
            print('|')
            print('|')
            print(' '.join(hiden_word))
            bad_or_good_choice()
        if chances == 8:
            print('._________.')
            print('|         |')
            print('|         |')
            print('|         |')
            print('|_________|')
            print(' '.join(hiden_word))
            bad_or_good_choice()
        if chances == 7:
            print('._________.')
            print('|      |  |')
            print('|         |')
            print('|         |')
            print('|_________|')
            print(' '.join(hiden_word))
            bad_or_good_choice()
        if chances == 6:
            print('._________.')
            print('|     _|  |')
            print('|         |')
            print('|         |')
            print('|_________|')
            print(' '.join(hiden_word))
            bad_or_good_choice()
        if chances == 5:
            print('._________.')
            print('|    o_|  |')
            print('|         |')
            print('|         |')
            print('|_________|')
            print(' '.join(hiden_word))
            bad_or_good_choice()
        if chances == 4:
            print('._________.')
            print('|    o_|  |')
            print('|    |    |')
            print('|         |')
            print('|_________|')
            print(' '.join(hiden_word))
            bad_or_good_choice()
        if chances == 3:
            print('._________.')
            print('|    o_|  |')
            print('|   -|    |')
            print('|         |')
            print('|_________|')
            print(' '.join(hiden_word))
            bad_or_good_choice()
        if chances == 2:
            print('._________.')
            print('|    o_|  |')
            print('|   -|-   |')
            print('|         |')
            print('|_________|')
            print(' '.join(hiden_word))
            bad_or_good_choice()
        if chances == 1:
            print('._________.')
            print('|    o_|  |')
            print('|   -|-   |')
            print('|   /     |')
            print('|_________|')
            print(' '.join(hiden_word))
            bad_or_good_choice()
        if chances == 0:
            print('._________.')
            print('|    o_|  |')
            print('|   -|-   |')
            print('|   / \   |')
            print('|_________|')
            print('You Lose! :(')
            print('This word was:' + r_word)
            again = input('If u want try again press Y: ')
            if again == 'Y' or 'y':
                hangman()
            else:
                break


playerName = input('Enter your name: ')
print('Welcome ' + playerName + '!')
time.sleep(1)

hangman()