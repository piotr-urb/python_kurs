# Napisz funkcję, która zapyta o ocenę książki i wyświetli książkę wraz z oceną, jeżeli książka o takiej ocenie istnieje
def add_book():
    dict_books = {}
    counter = int(input(" Ile Książek chcesz dodać :"))
    for i in range(counter):
        title = input("Podaj tytuł Książki:")
        grade = input("Podaj ocenę: ")
        dict_books[title] = grade
    return dict_books

def read_book_by_grade(libr):
    g = input("Podaj ocenę ksiązki jaką chcesz przeczytać: ")
    if g in libr.values():
        for title, grade in libr.items():
        if grade == g:
            pritn(title, "- ocena", grade)
    else:
        print("Nie ma książki o takiej ocenie")

books = add_book()
print(books)
read_book_by_grade(books)


