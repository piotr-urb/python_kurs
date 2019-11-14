import random
class Dog:
    tail = True
    def __init__(self, name, breed, age, color):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color

    def pseudo(self):
        adj = ["destroyer", "powerfull", "funny", "sweet"]
        return self.name + "-" + random.choice(adj)
    def bark (self):
        bark = " Hau " * random.randint(1, 15)
        return bark

    def tail (self):
        tail_mach = " mach " * random.randint(1,20)
        return tail_mach

obj_pimpek = Dog("Pimpek","Collie",5,"white")
obj_dyzio = Dog("Dyzio", "Cotton de Tulear", 7, "Blond")
print(obj_pimpek.name)
print(obj_pimpek.tail)
print(Dog.pseudo(obj_dyzio))
print(Dog.bark(obj_pimpek))
print(Dog.tail(obj_dyzio))

# names = "Anna, Marta, Marek, Paweł"
# print(names.split(","))
# print(type(names))
# print(str.split(names, ","))
