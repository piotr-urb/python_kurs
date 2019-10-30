#Dopuki  temp != 200 rób
#zmienna która przechowuje celciusze
#zmienna z temp farenhaita
#wyświetl (temp_Fahr,"=", temp_C)
#aktualizuj temp_Fahr co 20
temp_C = 0
temp_F = 0

while temp_F <= 200 :
        temp_C = round((5/9)*(temp_F-32),2)
        print(temp_F, "F=", temp_C,"C")# wyświetlenie
        temp_F=temp_F+20 # aktualizacja

