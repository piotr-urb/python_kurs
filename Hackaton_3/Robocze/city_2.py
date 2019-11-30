import tavern as t
import order as o
import random


def roll_the_dice():
    cubes_wall = ['1', '2', '3', '4', '5', '6']
    dice_number = random.choice(cubes_wall)
    return dice_number

def enter_the_city():
    print("You arrive in to a small town chose where you want to go")
    print("1 - Go to a tavern if you want to buy food or weapon or play a dice ")
    print("2 - Go to an Order if you want to know what is your mission, if you don't know what to doo ")
    print("What is your answer: \n")
    decision = input()
    if decision == "1":
        t.enter_the_tavern()
    elif decision == "2":
        o.enter_the_order()
    else:
        print("Wrong choice try again")
        enter_the_city()

enter_the_city()