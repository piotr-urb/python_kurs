# Utwórz dekorator @uppercase_decorator, który przyjmuje dowolną funkcję zawracającą
# # łańcuch znaków i zwracający ten sam tekst zmieniony na wielkie litery.
# # Utwórz funkcję zwracającą tekst
# # Utwórz dekorator przyjujący tę funkcję
# # Wywołaj funkcję, by sprawdzić, że decorator działa


def uppercase_decorator(text):
    def big_letters():
        big_text = text().upper()
        print("Jestem w funkcji")
        return big_text
    return big_letters


@uppercase_decorator
def return_text():
    text = input("Podaj tekst :")
    return text

print(return_text())

# big = uppercase_decorator(return_tekst)
# # print(big())
#