#Zadanie nr 5:
#	5▹ Stwórz grę ciepło zimno.
#	Komputer losuje liczbę z zakresu od 1 do 100.
#	Użytkownik podaje swój traf.
#	Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
#	Jeśli użytkownik zgadnie wygrywa gracz.
#	Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.
import random
import math

def lotery():
    number = range(100)
    arg = random.choice(number)
    print("Komputer randomly choose number : ", arg)

    return arg
komp_choice = lotery()
user_choice = input()
for a in range(komp_choice):
    print("What is your number")
    user_choice = input()
    if user_choice == komp_choice:
        print("Congratulation you win")
    elif user_choice != komp_choice:
        print("Try _again")
