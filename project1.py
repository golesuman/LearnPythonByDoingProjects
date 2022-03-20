import random
from tkinter.tix import MAX
from unicodedata import numeric
from wsgiref.util import guess_scheme

from sympy import sec




NUM_DIGITS=3
MAX_GUESSES=10
def main():

    while True:
        secretNum=getSecretNum()
        print('I have thought a number.')
        print(f'You have {MAX_GUESSES} gusses to guess it.')
        numGuesses=1

        while numGuesses<=MAX_GUESSES:
            guess=''
            while len(guess)!=NUM_DIGITS or not guess.isdecimal():
                print(f'Guess {numGuesses}')
                guess=input(">")
            clues=getClues(guess,secretNum)
            print(clues)
            numGuesses+=1

            if guess==secretNum:
                break
            if numGuesses>MAX_GUESSES:
                print('you have run out of guesses')
                print(f'The right number was {secretNum}')


        print("Do you want to play again? (yes or no)")
        if not input(">").lower().startswith('y'):
            break

        print('Thanks for playing !')

def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess,secretNum):
    if guess==secretNum:
        return 'You got it'

    clues=[]

    for i in range(len(guess)):
        if guess[i]==secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues)==0:
        return "Bangles"

    else:
        #sort the clues into alphabetical order so their original order
        # doesn't give any information away

        clues.sort
        return ''.join(clues)




if __name__ == '__main__':
    main()




