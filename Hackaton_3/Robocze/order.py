import mine as m
import river as r


def enter_the_order():
    print("Nice to meet you a stranger, please I had some mission to you")
    print("Chose one of the mission below:")
    print("1- Mission nr 1 - River")
    print("2- Mission nr 2 - Gold Mine")
    answer = input("Please what is your answer:")
    if answer == "1":
        r.river()
    elif answer == "2":
        m.mine()