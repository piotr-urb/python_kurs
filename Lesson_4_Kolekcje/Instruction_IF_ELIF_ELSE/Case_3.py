number_1 = float (input("Oceń książkę w skali 1-10 ocena 1:"))
number_2 = float (input("Oceń książkę w skali 1-10 ocena 2:"))
number_3 = float (input("Oceń książkę w skali 1-10 ocena 3:"))
number = float((number_1 + number_2 + number_3)/3)
print (number)
if number >= 7 :
    print(" This book is very good")
elif number >= 5 :
    print(" This book is not good enough")
else :
    print(" This book is very bed ")

