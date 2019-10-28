
with open('tekst.txt', 'r') as fopen:
    while True:
        current_line = fopen.readline()

    # aktualna linia jest pusta
        if current_line == '':
    # dotarlismy do konca
            break
        print(current_line)