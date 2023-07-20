# guess a word from the collection of words by guessing characters one by one


import random
from collections import Counter

someWords = '''apple banana mango strawberry
orange grape pineapple apricot lemon coconut watermelon
cherry papaya berry peach lychee muskmelon'''


someWords = someWords.split(' ')
print(someWords)
word = random.choice(someWords)

chances = len(word)+2
print("you have total ",chances,"chances. Good Luck! ")

letterGuessed = ""
for _ in range(len(word)):
    print('_', end=' ')
print()
while chances > 0:
    chances -= 1

    guess = str(input("guess the character: "))
    if not guess.isalpha():
        print("enter letter only")
        continue
    elif len(guess) > 1:
        print("enter only one letter")
        continue

    if guess in word:
        k = word.count(guess)
        for _ in range(k):
            letterGuessed += guess

    for char in word:
        if char in letterGuessed and Counter(letterGuessed) != Counter(word):
            print(char, end=' ')
            print()
        elif Counter(letterGuessed) == Counter(word):
            print("Congrats you won!")
            print("the word ",word, "is found in ",chances,"chances")
            break
            break
        else:
            print('_', end=' ')
            print()

if chances <= 0 and Counter(letterGuessed) != Counter(word):
    print("you lose, try again ")






