# Guess the word by guessing alphabates one by one 

import random

name = input("what is your name? ")
print("Welcome "+name+" Guess the alphabates ")

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks', 'girls', 'comma']

word = random.choice(words)

turn = 12
guess = ""

while turn > 0:

    failed = 0
    for char in word:
        if char in guess:
            print(char)
        else:
            print('_')
            failed += 1

    if failed == 0:
        print("You Win!!!")
        print("the guess "+guess+" is found in ",turn,"tries ")

    a = input('guess a character: ')
    guess += a

    if a not in word:
        print("wrong ")
        turn -= 1
        print("you have ",turn,"turns left ")

        if turn == 0:
            print("you lose ")
