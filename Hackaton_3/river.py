def river():
    print(" Its take you 8 hours to got to the river, so your supply are diminish to half")
    print(" Suddenly form the river jump out the Dragon, you must fight with him, and you got hurt, he lost -2 life points")
    print(" You need some medical attention, suddenly you meet the fisherman")
    print(" Do you need help , answer y/n")
    answer = input()
    if answer == "y":
        print("The fisherman gave you some food, and medical attention, you fill better, you got back +1 of your life points")
    elif answer == "n":
        print("You loose some blood, you fill bad, you loos another -1 of your life points")
    else:
        print(" Wrong answer, think one more time")
        river()