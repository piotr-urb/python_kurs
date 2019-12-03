#Zadanie nr 2:
#2▹ Utwórz listę L_test = [1, 2, 3, 4], krotkę T_test = (1, 2, 3, 4) oraz set S_test = {1, 2, 3, 4}. Jakie metody dostępne dla typu list nie będą działać dla typów tuple i set?

L_test = [1, 2, 3, 4]
T_test = (1, 2, 3, 4)
S_test = {1, 2, 3, 4}

print("Lista:", L_test)
print("Tupla:", T_test)
print("Set:  ", S_test)

# len
print(len(L_test))
print(len(T_test))
print(len(S_test))
print("len () - działa dla wszystkich")

# append()
L_test.append('L_test')
print(L_test)
print("append(), działa tylko dla listy")

# insert()
L_test.insert(2, 'insert')
print(L_test)
print("insert(), działa tylko dla listy")

# remove()
L_test.remove(1)
print(L_test)
print("remove(), działa tylko dla listy")

# index()
print('Lista: ', L_test.index(2))
print('Tupla: ', T_test.index(2))
print("index(), działa dla listy i krotki")

# count()
print('Lista: ', L_test.count(2))
print('Tupla: ', T_test.count(2))
print("count(), działa dla listy i krotki")

# # reverse()
# L_test.reverse()
# print(L_test)
print("reverse(), działa jedynie dla listy")

# extend()
L_test.extend(['extend', 'extend', 'extend', 1,2,2,3,34])
print(L_test)
print("extend(), działa jedynie dla listy")