# Adress book:

address_book = [{'Surname' : 'Kowalski', 'Name' : 'Jan', 'Phone' : '123456789', 'address': 'jan.kowalski@wp.pl', 'City' : 'Poznań'},
                {'Surname' : 'Mickiewicz', 'Name' : 'Adam', 'Phone' : 'unknown','address': 'adam.mickiewicz@wp.pl','City' : 'Cemetery'},
                {'Surname': 'Kowal', 'name':'Piotr', 'Phone': '889920963', 'adress': 'piotr.kowal@wp.pl', 'City':'Warszawa'}]
def go_to_selection():
    print()
    print(main_menu())
    print()
    selection = input(("Enter your selection:"))
    if selection == "1":
        show_all()
    elif selection == "2":
        add_record()
    elif selection == "3":
        remove_rec()
    elif selection == "4":
        exit_program()
    else:
        print("Wrong selection, try again from 1 to 4")
        go_to_selection()

# main function
def main_menu():
    return ("Main Menu"
            "\n1 - list all records"
            "\n2 - enter a new record"
            "\n3 - delete an exist record"
            "\n4 - exit")

#   - Wyświetlenie wszystkich wpisów
def show_all():
    counter = 1
    for rec in address_book:
        print(counter, rec)
        counter += 1
    go_to_selection()

 #  - Stworzenie nowego wpisu (dane wczytywane z klawiatury)
def add_record():
    counter = int(input('How many records do you want to add?'))
    adding = 1
    while adding <= counter:
        address_book.append({'Surname' : input('Surname: '), 'Name' : input('Name: '), 'Phone' : input('Phone number: '), 'City' : input('City: ')})
        adding += 1
    show_all()

# - Usunięcie wpisu

def remove_rec():

    to_remove = int(input('Which record do you want to remove? '))
    if to_remove > len(address_book):
        print('Record not found!')
        go_back = input('Do you want to try again? y/n: ')
        if go_back == 'y':
            remove_rec()
        else:
            go_to_selection()
    else:
        del address_book[to_remove - 1]
        show_all()
#  - Zakończenie pracy programu
def exit_program ():
    print('See you next time!')

go_to_selection()