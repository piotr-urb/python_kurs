#(part: if, elif, Else)
#Zadanie nr 4:
#Utwórz zmienną przechowującą dowolny ciąg znaków.
#Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a.
#Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.

print("Podaj dowolny string:")
string = str(input())
if len(string) > 5:
    print("String is longest then 5 letters")
else:
    print("String is shorter then 5 letters")

letter = 'a'
list = ''
if letter in string:
    print("****************************")
    print(string)
    list = string.split(string, len(string))
    print(list)
else:
    print("----------------------------")
    print(string)