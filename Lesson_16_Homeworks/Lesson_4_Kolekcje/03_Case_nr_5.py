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

for word in words:
    if word not in occurrence:
        occurrence[word] = 1
    else:
        occurrence[word] += 1

print()
for el1, el2 in occurrence.items():
    print(el1, ":", el2)

    #/////////////////////////////////////////////////
    # zadanie 5

    text = """Szybko, zbudź się, szybko, wstawaj
    Szybko, szybko, stygnie kawa
    Szybko, zęby myj i ręce"""

    # 1. tworzymy pusty słownik: words = {}
    # 2. txt -> przechowuje tekst wierszyka
    # 3. txt -> dzielimy na osobne wyrazy, np split -> dostajemy listę w efekcie
    # 4. for -> lista elementów txt
    # sprawdza czy słowo jest w słowniku
    # TAK: słownik[słowo] =+ 1
    # NIE: słownik[słowo] = 1
    # 5. ładne wyświetlanie jak w zadaniu

    words = {}
    text = text.replace(',', '').lower()
    wordlist = text.split()
    words['szybko'] = 0
    words['zbudź'] = 0

    for elem in wordlist:
        if elem == 'szybko':
            words['szybko'] += 1
        elif elem == 'zbudź':
            words['zbudź'] += 1

    for ke, va in words.items():
        print(ke, ':', va)