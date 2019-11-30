
import city as c


def vendor(player):
    print("Fat man sells some items. What do you want to browse?")
    browse = input("Choose what do you want to buy (weapon/food): ")
    weapon = player.weapon
    money = player.money
    life = player.life
    if browse.lower() == "weapon":
        print(weapon)
        buy = input("Do you want to buy something? (y/n)")
        if buy == "y":
            what = input("What item do you want to buy? Enter it's full name: ")
            print(what in weapon)
            if (what in weapon) == True:  
                print("Price", weapon.get(what))
                if (money - int(weapon.get(what))) < 0:
                    print("You have not enough money!")
                    vendor()
                else:
                    money = int(money) - int(weapon.get(what))
                    weapon == (weapon + ", " + what)
                    print("New sald", money)
                    c.enter_the_tavern()
            else:
                print("No such item")
                vendor()
        else:
            print("Sees that items sold here are plain garbage. No need to waste precious {purse} gold coins.")
            c.enter_the_tavern()
    elif browse.lower() == "food":
         print(food)
         buy = input("Do you want to buy something? (y/n)")
         if buy == "y":
             what = input("What item do you want to buy? Enter it's full name: ")
             print(what in food)
             if (what in food) == True:
                print("Price", food.get(what))
                if (money - int(food.get(what))) < 0:
                    print("You have not enough money!")
                    vendor()
                else:
                    food = (int(food) + int(food.get(what)))
                    food == (food + ", " + what)
                    life = life + food
                    print("Nowe sald", food)
                    c.enter_the_tavern()
             else:
                 print("No such kind of food")
                 vendor()
         else:
            print("Sees that items sold here are plain garbage. No need to waste precious {purse} gold coins.")
            c.enter_the_tavern()


food = {
    "Duck" : 40,
    "Chicken" : 80,
    "Bananas" : 20
}

weapon = {
    "Stick" : 10,
    "Club" : 30,
    "Rusty sword" : 50,
    "Sharp knife": 100,
    "Longsword" : 300
}
vendor(player)