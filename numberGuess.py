#Build a Number guessing game, in which the user selects a range.
#Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
#Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses

import random
import math

a  = int(input('first number: '))
b  = int(input('second number: '))

c = random.randint(a,b)

minGuess = int(math.log(b-a+1, 2));
print("You can not have more than ",minGuess,"guesses")

cnt = 0;

while cnt < minGuess:

    guess = int(input("guess the number: "))
    if guess > c:
        print("number is too big!!")
    elif guess < c:
        print("number is too small!!")
    else:
        print("Congratulations you guessed it right in ", cnt+1, "tries")
        break;
    cnt += 1

if cnt == minGuess:
    print("Better luck next time")


