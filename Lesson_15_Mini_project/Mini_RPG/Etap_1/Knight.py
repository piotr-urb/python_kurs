class Knight:
    def __init__(self, life, experiences):
        self.life = 60
        self.experiences = 0

    def __repr__(self):
        return f"Knight: hp = {self.life}, exp={self.experiences}"

    def march(self, distance):
        print(f"Knight walks  {distance}m")
        self.experiences += 0.2*distance

    def attack(self):
        print(f" The Knight is Waving a sword!")
        self.experiences += 0.3

def main():
    p = Knight()
    print(p)
    p.march(10)
    print(p)
    p.attack()
    print(p)

if __name__ == '__main__':
            main()