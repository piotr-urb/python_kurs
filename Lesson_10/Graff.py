#Graf
# dom = 0
# szkoła = 1
# kościół = 2
# bar = 3
# szpital = 4
# kino = 5
# teatr = 6

graff = [[0, 1, 1, 1, 0, 0, 0],
         [1, 0, 0, 0, 1, 0, 0],
         [1, 0, 0, 1, 0, 1, 0],
         [1, 0, 1, 0, ],
         [],
         [],
         [],
         ]
for row in range(7):
    print(lista_obiektów[row], ":")
    #print(graph[row])
    for col in range(7):
        if graph[row][col] == 1:
            print(lista_obiektów[row], "---", lista_obiektów[col])
