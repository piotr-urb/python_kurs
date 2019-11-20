#(Listy - moduły)
#Zadanie nr 2:
#2▹ Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.
print("Potrzebnych jest 10 liczb:")
list = []
list_2 = []
i = 0
while int(i) < 10:
    print(" Podaj liczbę:")
    a = input()
    if int(a)%2 == 0:
        list_2.append(a)
    else:
        list.append(a)
    i = i+1
print("Lista elementów niepażystych:",list)
print("Lista elementów parzystych:", list_2)
