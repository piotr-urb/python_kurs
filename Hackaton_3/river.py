import random

def river(player,dragon):
    print(" Its take you 8 hours to got to the river, so your supply are diminish to half, you fill weak, your life is -10 points")
    player.life = player.life - 10
    print("Now you have a:", player.life)
    print(" Suddenly form the river jump out the Dragon, you must fight with him or you can run what is your answer?")
    answer = input("Will you fight fight/run?\n")
    if answer.lower() == "fight":
        a = dragon_damage()
        b = gamer_damage()
        player.life = int(player.life) - int(a)
        print(player.life)
        dragon.life = int(dragon.life) - int(b)
        print(dragon.life)
        print(f"The Dragon hurt you and takes:{damage}points of life\n")
        print("The player life is", player.life)
        print("***************************")
        print("The fisherman gave you some food, and medical attention, you fill better, you got back +1 of your life points")
        print(" You need some medical attention, suddenly you meet the fisherman")
        print(" Do you need help , answer y/n")
    elif answer.lower() == "run":
        print("You loose some blood, you fill bad, you loos another -10 of your life points")
        player.life -= 10
        print(player.life)
    else:
        print(" Wrong answer, think one more time")
        river(player)

    return player.life


class Dragon:
    def __init__(self, life):
        self.life = 200



def dragon_damage():
    dragon = ["30", "50", "70", "90", "110", "130"]
    damage = random.choice(dragon)
    print("The Dragon hits the Player and makes points of damage:", damage)
    return damage

def gamer_damage():
    gamer = ["30", "50", "70", "90", "110", "130"]
    damage = random.choice(gamer)
    print("The Player hits the Dragon and makes points of damage:", damage)
    return damage


# print(gamer_damage())
# print(dragon_damage())