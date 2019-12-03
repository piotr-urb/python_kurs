#Zadanie nr 4:
#4▹ Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.
print("Podaj parzysta liczbę elementów, poszczególne elementy oddziel od siebie przecinkiem :\n")
list_el = input()
list_el = list_el.split(',')
el_1 = list_el[len(list_el)//2-1]
el_2 = list_el[len(list_el)//2]

if el_1 == el_2:
    print("Środkowe elemety sa takie same")
else:
    print("Środkowe elementy maja różne warości")
print("Element nr 1 :", el_1)
print("Element nr 2 :", el_2)
# while int(i)%2 != 0:
#     print ("Podaj element listy:")
#     a = input()
#     list_el.append(a)
#     print(len(list_el))
# # b = list.index((len(list)/2))
# print(b)