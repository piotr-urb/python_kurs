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


obj_pimpek = Dog("Pimpek","Collie",5,"white")
obj_dyzio = Dog("Dyzio", "Cotton de Tulear", 7, "Blond")
print(obj_pimpek.name)
print(obj_pimpek.tail)
#print(obj_pimpek.pseudo())
#print(obj_dyzio.pseudo())
#print(obj_dyzio.tail)
print(Dog.pseudo(obj_dyzio))
names = "Anna, Mart, Marek, Paweł"
print(names.split(","))
print(type(names))
print(str.split(names, ","))


#print(Dog.tail)
#print(obj_dyzio.__dict__)
#print(Dog.p__dict__)

# print(obj_pimdyzioek)
# print(obj_dyzio)
# a = 12
# print(type(a))
# print(type(obj_dyzio))
# print(type(obj_pimpek))
# obj_pimpek.name = "Pimpek"
# obj_pimpek.breed = "Jamnik"
# obj_pimpek.age = 12
# obj_pimpek.color = "brown"