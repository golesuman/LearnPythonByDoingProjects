from time import *
import random as r
from turtle import speed

def mistake(paragraph, userinput):
    error = 0
    for i in range(len(paragraph)):
        try:
            if paragraph[i] != userinput[i]:
                error = error + 1
        except:
            error = error + 1
    return error
    

def speed_time(time_start, time_end, userinput):
    time_delay = time_end - time_start
    time_roundoff = round(time_delay, 2)
    speed = len(userinput) / time_roundoff
    return round(speed)


def main():
    test = ['hey this is suman', 'this is one of the best trip i have done in a while', 'man this is lit',
    'man I want to do this again.']


    test1 = r.choice(test)
    print("*****  typing speed calculator  ******")
    print(test1)
    print()
    print()
    time_1 = time()
    testinput = input("Enter : ")
    time_2 = time()
    print(f"Speed : {speed_time(time_1, time_2, testinput)} words/sec")
    print(f"Error: {mistake(test1, testinput)}")

if __name__ == '__main__': 
    main()
