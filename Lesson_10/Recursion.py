def wypisz(n):

    if n < 0:
        print("-")
        n = -n
    elif n/10 != 0:
        wypisz(n/10)
        print("Wartość" : {n % 10}")
wypisz(123)


