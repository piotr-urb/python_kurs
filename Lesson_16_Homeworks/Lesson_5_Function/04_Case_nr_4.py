# 4▹ Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie.
# Powinna zwrócić komunikat: “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”.

def num_range (a, b):
    new_range = range(a, b)
    return new_range

def check_range(number):
    c = int(input('Podaj liczbę do sprawdzenia: '))
    num_range(a, b)
    if a < c < b:
        return 'Liczba', c, 'znajduje się w zakresie.'
    else:
        return 'Liczba', c, 'jest poza zakresem.'

a = int(input("Podaj dolna wartość zakresu do sprawdzenia:\n"))
b = int(input("Podaj górną wartość zakresu do sprawdzenia:\n"))
number = num_range(a, b)
print(check_range(number))
