przedmioty= input(" podaj  przedmioty rozdzielone :")
oceny = input( "podaj oceny podzielone myślnikiem :")
przedmioty = przedmioty.split("-")
oceny = oceny.split("-")
licznik = 0

while (licznik <3):
    print (przedmioty[licznik], oceny[licznik])
    licznik += licznik

