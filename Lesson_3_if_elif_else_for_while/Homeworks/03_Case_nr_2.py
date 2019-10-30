#(petla while)
#Zadanie nr 2:
#2) Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie (np. secret_num = 5). Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.
secret_number = '7'
print("Podaj numer od 1 do 20:")
number = str(input())
while number != secret_number:
    print("Spróbuj jeszcze raz, podaj numer:")
    number = str(input())