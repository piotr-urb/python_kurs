
#6▹ Napisz grę kamień-papier-nożyce tak, aby korzystać z funkcji.

import random

def lotery():
    figures = ['k', 'p', 'n']
    arg = random.choice(figures)
    print("I randomly choose figure : ", arg)
    return arg

def function_1(user_choice, komp_choice):


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
            elif user_choice == 'n' and komp_choice == 'n':
                print("It is unsolved game: ")
                user_score = user_score + 0
                komp_score = komp_score + 0
                print("Komputer score:", komp_score)
                print("User score:", user_score)
            else:
                print("Your choice is incorrect try again")



def main():

    print("Wybierz jedną z trzech opcji:")
    print("Jeżeli wybierasz kamień nacisnij - k:")
    print("Jeżeli wybierasz nożyce nacisnij - n:")
    print("Jeżeli wybierasz papier nacisnij - p:")
    print("Aby przerwać zakończyc rozgrywke napisz: koniec")
    print("how many rounds you want to  play:")
    round = input()
    user_score = 0
    komp_score = 0
    a = 0
    for a in range(int(round)):
        user_choice = input("Chose an option :\n")
        print("User choice is:", user_choice)
        komp_choice = lotery()
        print("Computer choice is:",komp_choice)
        function_1(user_score, komp_score)
    a = a + 1
main()