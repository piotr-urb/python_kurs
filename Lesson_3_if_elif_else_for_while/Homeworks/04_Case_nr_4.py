#Zadanie nr 4:
#4▹ Napisz grę - kamień (k) / papier (p) / nożyce (n).
#Użytkownik podaje jedną z 3 figur.
#Komputer losuje jedną z 3 figur.
#Sprawdź kto wygrał tę rundę.
#Zmień kod tak, by użytkownik mógł podac liczbę rund.
#Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
#Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’
import random

def lotery():
    figures = ['k', 'p', 'n']
    arg = random.choice(figures)
    print("I randomly choose figure : ", arg)
    return arg

print("Wybierz jedną z trzech opcji:")
print("Jeżeli wybierasz kamień nacisnij - k:")
print("Jeżeli wybierasz nożyce nacisnij - n:")
print("Jeżeli wybierasz papier nacisnij - p:")
print("Aby przerwać zakończyc rozgrywke napisz: koniec")
print("how many rounds you want to  play:")
round = input()
user_score = 0
komp_score = 0


for a in range(int(round)):
    print("Chose an option :")
    user_choice = input()
    komp_choice = lotery()

    if user_choice == 'koniec':
        print("Komputer score:", komp_score)
        print("User score:", user_score)
        break
    else:
        if user_choice == 'k' and komp_choice == 'k':
            print("It is unsolved game: ")
            user_score = user_score + 0
            komp_score = komp_score + 0
            print("Komputer score:", komp_score)
            print("User score:", user_score)
        elif user_choice == 'k' and komp_choice == 'n':
            print("User win this game: ")
            user_score = user_score + 1
            komp_score = komp_score + 0
            print("Komputer score:", komp_score)
            print("User score:", user_score)
        elif user_choice == 'k' and komp_choice == 'p':
            print("Komputer win this game: ")
            user_score = user_score + 0
            komp_score = komp_score + 1
            print("Komputer score:", komp_score)
            print("User score:", user_score)
        elif user_choice == 'p' and komp_choice == 'k':
            print("User win this game: ")
            user_score = user_score + 1
            komp_score = komp_score + 0
            print("Komputer score:", komp_score)
            print("User score:", user_score)
        elif user_choice == 'n' and komp_choice == 'k':
            print("Komputer win this game: ")
            user_score = user_score + 0
            komp_score = komp_score + 1
            print("Komputer score:", komp_score)
            print("User score:", user_score)
        elif user_choice == 'p' and komp_choice == 'p':
            print("It is unsolved game: ")
            user_score = user_score + 0
            komp_score = komp_score + 0
            print("Komputer score:", komp_score)
            print("User score:", user_score)
        if user_choice == 'n' and komp_choice == 'n':
            print("It is unsolved game: ")
            user_score = user_score + 0
            komp_score = komp_score + 0
            print("Komputer score:", komp_score)
            print("User score:", user_score)
        else:
            print("Your choice is incorrect try again")
    a = a+1