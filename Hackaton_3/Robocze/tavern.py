import dice as d
import vendor as v

def enter_the_tavern():
    print("You arrived in to a small tavern. Here you can buy items and food or play dice for money.")
    answer = input("What do you want to do? (buy/play): ")
    if answer == "buy":
        v.vendor()
    elif answer == "play":
        d.role_dice()
        #tavern_play()
    else:
        print("There is no other options , try again")
        enter_the_tavern()
enter_the_tavern()
#
# def play():
#     user_dice_number = roll_the_dice()
#     print("Your dice number:", user_dice_number)
#     tawern_man_dice_number = roll_the_dice()
#     print("Tavern man dice number:", tawern_man_dice_number)
#     if int(user_dice_number) > int(tawern_man_dice_number):
#         winner = "user"
#         return winner
#     elif int(user_dice_number) < int(tawern_man_dice_number):
#         winner = "tavern_man"
#         return winner
#     else:
#         winner = "0"
#         return winner
#
# def gold_purse(money):
#     global purse
#     purse = int(purse) + int(money)
#     print("You have " + str(purse) + " zł on your count")
#     return purse
#
#
# def tavern_play():
#     print("You go to a tavern and you meet a man who sad: Roll the dice, if you win , then I will tale you what to do next")
#     choice = input(" Do you wont to play y/n:")
#     if choice == 'y':
#         print("Lest play then")
#         winner = play()
#         if winner == "user":
#             print(" You win you should go to the river, you got an extra money")
#             money = 40
#             print(gold_purse(money))
#             print(" When you got to hte river look after the fisherman, he will gave you some answers and help ")
#             r.river()
#
#         elif winner == "tavern_man":
#             print(" You loose you need to pay me for information - 20 zł: ")
#             money = -20
#             print(gold_purse(money))
#             print(" You should go back to your home")
#         elif winner == "0":
#             print(" You have lucky lets play again")
#             play()
#
#     elif choice == 'n':
#         print("It was a bad choice, you have two doors to chose to go out from here")
#         print("Chose one of the doors , select the number: 1 or 2 :")
#         answer = input()
#         if answer == "1":
#             print("You chose door number 1 - you will go to the dungeons you have to kill a dragon")
#             print("You need too chose your weapon")
#         elif answer == "2":
#             print("You chose door number 2 - you will go out on the desert you have to buy a water for 50 zł to stay alive")
#             player.money += -50
#             print(gold_purse(money))
#             if  gold_purse(money) >= 0:
#                 print(" Here is your water good luck")
#                 print(" When you go through the desert, you should find the : Human City")
#             else:
#                 print("You have not enough money to bay a watter, you will die")
#                 print("It, was pleasure to meet you , you loose you are a death man")
#                 print("END of GAME")
#     else:
#         print("Wrong choice try again")
#         tavern_play()