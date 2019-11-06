lista_obiektów = ["dom","szkoła","kościół"," bar","szpital", "kino", " teart"]

graph = [(0,1),(0,2),(0,3),(1,4),(2,3)]
for i in graph:
    b1, b2 = i
    print(lista_obiektów[b1], "---", lista_obiektów[b2])