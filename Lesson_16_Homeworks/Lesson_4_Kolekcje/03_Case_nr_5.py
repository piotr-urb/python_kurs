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
word_c = {}
text = text.replace(",", "").lower()
words_list = text.split()
word_c['szybko'] = 0
word_c['zbudź'] = 0
word_c['się'] = 0
word_c['wstawaj'] = 0
word_c['stygnie'] = 0
word_c['kawa'] = 0
word_c['zęby'] = 0
word_c['myj'] = 0
word_c['i'] = 0
word_c['ręce'] = 0

for word in words_list:
    if word == "szybko":
        word_c['szybko'] += 1
    elif word == "zbudź":
        word_c['zbudź'] += 1
    elif word == "się":
        word_c['się'] += 1
    elif word == "wstawaj":
        word_c['wstawaj'] += 1
    elif word == "stygnie":
        word_c['stygnie'] += 1
    elif word == "kawa":
        word_c['kawa'] += 1
    elif word == "zęby":
        word_c['zęby'] += 1
    elif word == "myj":
        word_c['myj'] += 1
    elif word == "i":
        word_c['i'] += 1
    elif word == "ręce":
        word_c['ręce'] +=1
for word, word_c in word_c.items():
    print(word,'-',word_c)


