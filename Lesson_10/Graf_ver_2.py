lista_obiektów = ["dom","szkoła","kościół"," bar","szpital"]

graph = [
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 1],
]
for row in range(4):
    print(lista_obiektów[row], ":")
    #print(graph[row])
    for col in range(5):
        if graph[row][col] == 1:
            print(lista_obiektów[row], "---", lista_obiektów[col])