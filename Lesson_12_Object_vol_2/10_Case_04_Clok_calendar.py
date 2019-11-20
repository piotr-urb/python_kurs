#4▹ Utwórz klasę zegaro-kalendarza. Zegaro-kalendarza łączy cechy zegara oraz kalendarza.
# Zaimplementuj dziedziczenie wielokrotne. Nasz zegaro-kalendarza powinen móc podawać aktualną datę
# oraz wyświetlać ile dni ma dany miesiąc. Dodatkowo utwórz sposób wyświetlania tak, aby zegaro-kalendarz
# zawierał datę, godzinę oraz widok dni ułożonych tygodniowo. Dla uproszczenia przyjmij 7 dni w tygodniu
# zawsze zaczyna się od pierwszego dnia.

import datetime


class Zegarek():
    def __init__(self):
        print("Zegarek")
    def current_time(self):
        return datetime.datetime.now().time()
class Kalendarz():
    def __init__(self):
        pass
    def current_date(self):
        return datetime.datetime.now().date()

class Zegarko_kalendarz(Zegarek, Kalendarz):
    def current_date_time(self):
        print(super().current_date())
        print(super().current_time())

zk = Zegarko_kalendarz()
print(zk.current_time())
print(zk.current_date())
print(zk.current_date())
print(zk.current_date())
