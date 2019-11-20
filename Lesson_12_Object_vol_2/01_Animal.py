# Klasa kręgowce
class Vertebrate:
    backbone = True
    def __init__(self):
        print("Random kręgowiec...")
    def __str__(self):
        return "I'm Vertebrate"

class Cat(Vertebrate):
    def __init__(self, name):
        self.name = name
    def sound(self):
        return "miau"

kitty = Cat("Kitty")
print(kitty.backbone)
