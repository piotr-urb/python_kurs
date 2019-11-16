#RPG
import random
def lottery():
    numbers = ['1', '2']
    arg = random.choice(numbers)
    print("I randomly choose number : ", arg)
    select_character(arg)


def roll_the_dice():
    cubes_wall = ['1', '2', '3', '4', '5', '6']
    dice_number = random.choice(cubes_wall)
    print("You rolled the dice dropped out: ", dice_number)
    return dice_number

def name_choice(name):
    print(" This are the names for you ")
        if name == '1':
            human_m_names = ["Zygfryd", "Gerwazy", "Zawisza"]
            print(human_m_names)
        elif    == '2':
            human_f_names = ["Anna", "Rita", "Yennefer"]
            print(human_f_names)
        elif select == '3':
            orc_m_names = ["Wrukag", "Zargulg", "Sunuguk"]
            print(orc_m_names)
        elif selec == '4':
            orc_f_names = ["Grat", "Yazgash", "Burzob"]
            print(orc_f_names)
        elif select == '5':
            elf_m_names = ["Methild", "Almon", "Elre"]
            print(elf_m_names)
        elif dice_number == '6':
            elf_f_names = ["Caeda", "Shenarah", "Ayda"]
            print(elf_f_names)
        else:
            print("There is no such option, try again")







def women_story():
    print("This is the Women Story")
    race_choice(select)
    print("Put your name ")
    name = input()
    print(name)
    name_choice()
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
        women_story()



def race_choice(select):
    print("What is your race please select from option")
    print(" 1 - If you are an Orc")
    print(" 2 - If you are an Human")
    print(" 3 - If you are an Elf")
    if select == '1':
        print(" You are from the Orc race ")
        return "Orc"
    elif select == '2':
        print(" You are from the Human race")
        return "Orc"
    elif select == '3':
        print(" You are form the Elf race ")
        return "Orc"
    else:
        race_choice(select)


def man_story():
    print("This is the Man Story")
    race_choice(select)
    name_choice(select)
    choose = input(" Do you wont to go to a Forest press y/n:")
    if choose == 'y':
        print("Lest go to a forest")
    elif choose == 'n':
        print("So what do you wont to do:")
    else:
        print("Wrong choice try again")
        man_story()
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
        man_story()




# Wybierz postać
def select_character(select):
    if select == '1':
        print(" You are the Women")
        women_story()
    elif select == '2':
        print(" You are a Man ")
        man_story()
    else:
        print(" Their is no such character i will chose it random")
        lottery()


def character_creator(select):
    print(" Who you want to be ?")
    print(" Select an option:")
    print(" 1 - Women")
    print(" 2 - Man")
    user_choice = input("Choose the character put number from 1 to 2:")
    select_character(user_choice)
    character_creator(select)

def main():
    print( "This is the Game ")
    character_creator()
main()
