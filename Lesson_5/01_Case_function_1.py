# Napisz funkcję, która pyta użytkownika o pary ksiązka + ocena i zapisuje w programie.
def add_book(dict_books):
    counter = int(input(" Ile Książek chcesz dodać :"))
    for i in range(counter):
        title = input("Podaj tytuł Książki:")
        grade = input("Podaj ocenę: ")
        dict_books[title] = grade
    return dict_books
books = {}
books = add_book(books)
print(books)

