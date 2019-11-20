# Klasa kręgowce
class Vertebrate:
    backbone = True
    def __init__(self):
        print("Random kręgowiec...")
    def desc(self):
        return "Zewnętrzną pokrywę ciała kręgowców stanowi skóra"

class Cat(Vertebrate):
    def __init__(self, name):
        print("kotek!")
        self.name = name
    def sound(self):
        return "miau"
    def desc(self):
        super().desc()
        print("Koty są super")
        super().__init__()

ver = Vertebrate()
kitty = Cat("Kitty")
print(kitty.backbone)
