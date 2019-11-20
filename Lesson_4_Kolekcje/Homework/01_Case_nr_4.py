#Zadanie nr 4:
#4▹ Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.
print("Podaj parzysta liczbę elementów:")
list = []
i = 0
while int(i)%2 != 0:
    print ("Podaj element listy:")
    a = input()
    list.append(a)
    print(len(list))
a = list.index((len(list)/2))
print(a)