class Animal:
    zoo = "Hayaton"

    def __init__(self, name, hunger=0):
        self._name = name
        self._hunger = hunger

    def get_name(self):
        return self._name

    def talk(self):
        pass

    def is_hungry(self):
        if self._hunger > 5:
            return True
        else:
            return False

    def feed(self):
        self._hunger -= 1


class Dog(Animal):

    def __init__(self, name, hunger):
        Animal.__init__(self, name)
        self._hunger = hunger
        self.type = "Dog"

    def talk(self):
        print("woof woof")
        self.fetch_stick()

    def fetch_stick(self):
        print("There you go sir")


class Cat(Animal):
    def __init__(self, name, hunger):
        Animal.__init__(self, name)
        self._hunger = hunger
        self.type = "Cat"

    def chase_laser(self):
        print("Meeeeow")

    def talk(self):
        print("meow")
        self.chase_laser()


class Skunk(Animal):
    def __init__(self, name, hunger, _stink_count=6):
        Animal.__init__(self, name)
        self._hunger = hunger
        self.type = "Skunk"

    def talk(self):
        print("tsssss")
        self.stink()

    def stink(self):
        print("Dear lord!")


class Unicorn(Animal):
    def __init__(self, name, hunger):
        Animal.__init__(self, name)
        self._hunger = hunger
        self.type = "Unicorn"

    def sing(self):
        print("I’m not your toy...	")

    def talk(self):
        print("Good day, darling")
        self.sing()


class Dragon(Animal):
    def __init__(self, name, hunger, _color="Green"):
        Animal.__init__(self, name)
        self._hunger = hunger
        self.type = "Dragon"

    def breath_fire(self):
        print("$@#$#@$")

    def talk(self):
        print("Raaaawr")
        self.breath_fire()


def main():
    zoo_lst = []
    brownie = Dog("Brownie", 10)
    zelda = Cat("Zelda", 3)
    stinky = Skunk("Stinky", 0)
    keith = Unicorn("Keith", 7)
    lizzy = Dragon("Lizzy", 1450)
    zoo_lst.append(brownie)
    zoo_lst.append(stinky)
    zoo_lst.append(zelda)
    zoo_lst.append(keith)
    zoo_lst.append(lizzy)
    zoo_lst.append(Dog("Doggo", 80))
    zoo_lst.append(Cat("Kitty", 80))
    zoo_lst.append(Skunk("Stinky Jr.", 80))
    zoo_lst.append(Unicorn("Clair", 80))
    zoo_lst.append(Dragon("McFly", 80))

    for animal in zoo_lst:
        while animal.is_hungry():
            animal.feed()
        print(str(animal.type) + " " + animal.get_name())
        animal.talk()

    print(Animal.zoo)


if __name__ == '__main__':
    main()
