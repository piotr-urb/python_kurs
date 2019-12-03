#Zadanie nr 5:
#5▹ W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.
#"""Szybko, zbudź się, szybko, wstawaj
#Szybko, szybko, stygnie kawa
#Szybko, zęby myj i ręce"""
#Zadbaj o sposób wyświetlania np.:
#szybko : 5
#zbudź : 1

text = """Szybko, zbudź się, szybko, wstawaj 
    Szybko, szybko, stygnie kawa 
    Szybko, zęby myj i ręce """

text = text.replace(",", "").lower()
words = text.split()
occurrence = {}

