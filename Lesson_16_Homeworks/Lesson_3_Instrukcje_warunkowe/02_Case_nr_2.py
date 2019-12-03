#(petla for)
#Zadanie nr 2:
#Utwórz listę, która zawiera składniki na ulubione danie. Wyświetl komunikaty co należy pokolei dodać. Poza pętlą umieść pozostałe instrukcje np. “Wrzuć do pierkanika”, “Podawaj schłodzone”.
print("Prosty przepis na naleśniki")
products = ["mąka", "jajka","mleko","woda", "sól","masło"]
for n in range(len(products)):
    print("Składnik nr:",n+1, products[n])

print("*********************************************************")
print(products[0] + " wsypać do miski, dodać " + products[1] + ", "+ products[2] + ", "+products[3] + ", " + products[4] +",:")
print("Zmiksować na gładkie ciasto. Dodać roztopione "+ products[5] + "lub olej roślinny i razem zmiksować lub wykorzystać tłuszcz do smarowania patelni przed smażeniem każdego naleśnika")
print("Naleśniki smażyć na dobrze rozgrzanej patelni z cienkim dnem np.   naleśnikowej. Przewrócić na drugą stronę gdy spód naleśnika będzie już ładnie zrumieniony i ścięty.")
