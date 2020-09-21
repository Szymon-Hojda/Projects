import time
import random
def hangman():
    words = [
    'baby','door','banana',
    'finger','fence','big',
    'swimming','pool','sun','church'
    ,'boy','bag',
    'alligator','mouse','birthday',
    'winter',"beach",'tree',
    'teacher','king',"telephone"]
    r_word = words[random.randint(0, len(words) - 1)] # Random word from words.
    chances = 10 # number of chances
    hiden_word = r_word
    hiden_word2 = '_' * len(r_word)
    hiden_word3 = [hiden_word2]
    def bad_choice():  # change chances -1 or show good letter
        if userInput not in r_word:
           chances -= 1
        elif userInput in r_word:
            position_of_letter = r_word.find(userInput)
            print(position_of_letter)
            print(len(hiden_word))
            hiden_word3[position_of_letter] = userInput

    while chances != 0:
        if chances == 10:
            print('')
            print('')
            print('')
            print('')
            print('')
            print(hiden_word3)
            print(r_word)
            userInput = input('Give me a letter: ')
            bad_choice()
        if chances == 9:
            print('._________.')
            print('|')
            print('|')
            print('|')
            print('|')
            print(hiden_word3)
            userInput = input('Give me a letter: ')
            bad_choice()
        if chances == 8:
            print('._________.')
            print('|         |')
            print('|         |')
            print('|         |')
            print('|_________|')
            print(hiden_word3)
            userInput = input('Give me a letter: ')
            bad_choice()
        if chances == 7:
            print('._________.')
            print('|      |  |')
            print('|         |')
            print('|         |')
            print('|_________|')
            print(hiden_word3)
            userInput = input('Give me a letter: ')
            bad_choice()
        if chances == 6:
            print('._________.')
            print('|     _|  |')
            print('|         |')
            print('|         |')
            print('|_________|')
            print(hiden_word3)
            userInput = input('Give me a letter: ')
            bad_choice()
        if chances == 5:
            print('._________.')
            print('|    o_|  |')
            print('|         |')
            print('|         |')
            print('|_________|')
            print(hiden_word3)
            userInput = input('Give me a letter: ')
            bad_choice()
        if chances == 4:
            print('._________.')
            print('|    o_|  |')
            print('|    |    |')
            print('|         |')
            print('|_________|')
            print(hiden_word3)
            userInput = input('Give me a letter: ')
            bad_choice()
        if chances == 3:
            print('._________.')
            print('|    o_|  |')
            print('|   -|    |')
            print('|         |')
            print('|_________|')
            print(hiden_word3)
            userInput = input('Give me a letter: ')
            bad_choice()
        if chances == 2:
            print('._________.')
            print('|    o_|  |')
            print('|   -|-   |')
            print('|         |')
            print('|_________|')
            print(hiden_word3)
            userInput = input('Give me a letter: ')
            bad_choice()
        if chances == 1:
            print('._________.')
            print('|    o_|  |')
            print('|   -|-   |')
            print('|   /     |')
            print('|_________|')
            print(hiden_word3)
            userInput = input('Give me a letter: ')
            bad_choice()
        if chances == 0:
            print('._________.')
            print('|    o_|  |')
            print('|   -|-   |')
            print('|   / \   |')
            print('|_________|')
            print('This word was:' + r_word)
            print('"///////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"')
            print('"///                                                   \\\"')
            print('"///  ||     ||||||| ||||||  ||||||  |||||| |||||||    \\\"')
            print('"///  ||     ||   || ||      ||      ||     ||   ||    \\\"')
            print('"///  ||     ||   || ||||||  ||||||  |||||| || |||     \\\"')
            print('"///  |||||| |||||||     ||      ||  ||     ||  \\     \\\"')
            print('"///                 ||||||  ||||||  |||||| ||   \\    \\\"')
            print('"///                                                   \\\"')
            print('"///////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"')
            again = input('If u want try again press Y')
            if again == 'Y' or 'y':
                hangman()
            else:
                break

playerName = input('Enter your name: ')
print('Welcome ' + playerName +'!')
time.sleep(1)
print('*' * 45)
print('Try to guess the word in less than 10 attemps')
print('*' * 45)

hangman()
