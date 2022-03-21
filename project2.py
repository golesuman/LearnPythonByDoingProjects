import random

def guess(x):
    random_num=random.randint(1,x)
    guess=0
    
    while guess!=random_num:
        guess=int(input(f"guess a number between 1 and {x} ")) 
        print(guess)
        if guess < random_num:
            print('Sorry guess again. Too low')

        elif guess > random_num:
            print("Sorry guess again. Too high")


    print(f"you have guessed the number {random_num}")


if __name__ == '__main__':
    guess(10)


