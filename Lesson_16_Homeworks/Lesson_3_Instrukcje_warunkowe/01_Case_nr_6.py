#Zadanie nr 6:
#Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie liczbę ukrytą przez programistę wyświetl komunikat “gratulacje!”, w przeciwnym razie wyświetl “pudło!”.

komputer_number = '65'
print(" Podaj liczbę od 1 do 100;")
number = str(input())
print("Your number is:", number)
if number == komputer_number:
     print("Gratulacje")
else:
     print("Pudło")