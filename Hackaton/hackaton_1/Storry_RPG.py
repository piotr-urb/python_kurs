# RPG Story
# Można wybrać jedną z 4 postci:
# 1 - Wizard
# 2 - Barbarian
# 3 - Knight
# 4 - Necromancer
# Jeżeli nie wybierzesz żadnej znich program wybierze za ciebie losowo
# Każda postąć ma inna historię ( inna funkcja).
# Narazie rozbudowałem trochę historię Wizard i Knight , Barbarian i Necromancer czekają na swoja kolej.
#

import random
def lottery():
    numbers = ['1', '2', '3', '4']
    arg = random.choice(numbers)
    print("I randomly choose number : ", arg)
    select_character(arg)


def roll_the_dice():
    cubes_wall = ['1', '2', '3', '4', '5', '6']
    dice_number = random.choice(cubes_wall)
    print("You rolled the dice dropped out: ", dice_number)
    return dice_number



def wizard_story():
    print("This is the Wizard Story")
    choose = input(" Do you wont to go to a Forest press y/n:")
    if choose == 'y':
        print("Lest go to a forest")
    elif choose == 'n':
        print("So what do you wont to do:")
    else:
        print("Wrong choice try again")
        wizard_story()


def barbarian_story():
    print("This is the Barbarian Story")
    print("If you wont to know what is your mission you need to go to the tavern, there will be a man in red hat")
    print("You went to a tavern and you meet a man who sad: Roll the dice and I will tale you what to do next")
    choice = input(" Do you wont to play y/n:")
    if choice == 'y':
        print("Lest play then")
        dice_number = roll_the_dice()
        if dice_number == '1':
            print(" You are a tomato eater ")
        elif dice_number == '2':
            print(" You are a radish eater ")
        elif dice_number == '3':
            print(" You are a radish eater ")
        elif dice_number == '4':
            print(" You are a radish eater ")
        elif dice_number == '5':
            print(" You are a radish eater ")
        elif dice_number == '6':
            print(" You are a radish eater ")

    elif choice == 'n':
        print("So what do you wont to do:")
        answer = input()
        print(answer)
    else:
        print("Wrong choice try again")
        barbarian_story()



def knight_food(select):
    if select == '1':
        print(" You are a bananas eater ")
    elif select == '2':
        print(" You are a tomato eater ")
    elif select == '3':
        print(" You are a radish eater ")
    else:
        print("You cant make a choice I will chose for you:")
        food = ['1', '2', '3']
        food_1 = random.choice(food)
        print("I randomly choose food for you : ", food_1)
        if food_1 == '1':
            print(" You are a bananas eater ")
        elif food_1 == '2':
            print(" You are a tomato eater ")
        elif food_1 == '3':
            print(" You are a radish eater ")


def knight_story():
    print("This is the Knight Story")
    choose = input(" Are you hungry?: y/n:")
    if choose == 'y':
        print("Choose the food:")
        print("Push 1 - to eat bananas")
        print("Push 2 - to eat tomato")
        print("Push 3 - to eat radish")
        select = input("Your choice is:")
        knight_food(select)
    elif choose == 'n':
        print("So what do you wont to do:")
    else:
        print("Wrong choice try again")
        knight_story()


def necromancer_story():
    print("This is the Necromancer Story")


# Wybierz postać
def select_character(select):
    if select == '1':
        print(" You are the Wizard")
        wizard_story()
    elif select == '2':
        print(" You are a Barbarian ")
        barbarian_story()
    elif select == '3':
        print(" You are a Knight ")
        knight_story()
    elif select == '4':
        print(" You are a Necromancer")
        necromancer_story()
    else:
        print(" Their is no such character i will chose it random")
        lottery()


def main_menu():
    print(" Who you want to bee ?")
    print(" Select an option:")
    print(" 1 - Wizard")
    print(" 2 - Barbarian")
    print(" 3 - Knight")
    print(" 4 - Necromancer")
    user_choice = input("Choose the character put number from 1 to 4:")
    select_character(user_choice)
main_menu()




