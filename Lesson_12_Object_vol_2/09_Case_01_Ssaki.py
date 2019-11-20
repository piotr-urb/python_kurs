#1▹ Korzystając z wikipedii utwórz klasy - Kot, Pies, Człowiek. Każda z nich powinna dziedziczyć
# z nadrzędnej klasy Ssaki. Klasa Ssaki powinna dziedziczyć z klasy Zwierzęta. Utwórz obiekty klas
# - kot, pies i człowiek, udowodnij, że rzeczywiście korzystają z klas rodziców.

class Annimals ():
    print("Animals")
    def __init__(self):
        print("We are animals")
    def __str__(self):
        print(" The kingdom of Animals")


class Mammals (Annimals):
    def __init__(self):
        print("Mammals Kingdom")
        super().__init__()

    def show_description(self):
        print("Mammals")

class Dog (Mammals):
    def __init__(self, name, age, breed):
        pirnt("This is the Dog")
    def show_description(self):
        super().show_description()
        print("Im, the Dog")

    # def bark(self, sound='uf'):
    #     print(sound * self.age)
    # print("I'm Dog")


class Cat (Mammals):
    def __init__(self):
        print("I'm Cat")
    # def miau (self, sound='uf'):
    #     print(sound * self.age)
    # print("Cat")



class Man (Mammals):
    def __init__(self):
        print("I'm Man")
        print(super().__init__())

# mm = Mammals()
# an = Annimals()
# c = Cat()
# d = Dog()
m = Man()
