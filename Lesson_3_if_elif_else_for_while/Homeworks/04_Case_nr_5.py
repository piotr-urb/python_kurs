#Zadanie nr 5:
#	5▹ Stwórz grę ciepło zimno.
#	Komputer losuje liczbę z zakresu od 1 do 100.
#	Użytkownik podaje swój traf.
#	Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
#	Jeśli użytkownik zgadnie wygrywa gracz.
#	Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.
import random

def lotery():
    secret_number = random.randint(1, 100)
    return secret_number

print("I thin abaut number from 1 to 100:")
komp_choice = int(lotery())
for a in range(1, 7):
    print("What is your choice try to guess the number:")
    user_choice = int(input())
    if user_choice < komp_choice:
        print("Your number is too low, its cold")
    elif user_choice > komp_choice:
        print("Your number is too high, its cold")
    else:
        break
if user_choice == komp_choice:
    print("Congratulation, You  guess the secret number:", komp_choice)
else:
    print("You loose, the number you should have guess:", komp_choice)