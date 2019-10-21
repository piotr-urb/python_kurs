# Napisać funkcję , która oblicza pole koła na podstawie zadranego promienia
r = float(input(" Podaj długość promienia koła : "))
def my_circle_field (arg):
    pi = 3.14
    pole = pi * arg ** 2
    return pole
print(my_circle_field (r))