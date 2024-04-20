class Animal:
    count_animals = 0

    def __init__(self, _name="Octavio"):
        self._name = _name
        self._age = 0
        Animal.count_animals += 1

    def get_age(self):
        return self._age

    def birthday(self):
        self._age += 1
    
    def set_name(self, _name):
        self._name = _name

    def get_name(self):
        return self._name


def main():
    first_animal = Animal("Shalt")
    second_animal = Animal()
    print(first_animal.get_name() + "\n" + second_animal.get_name())
    first_animal.set_name("Koral")
    print(first_animal.get_name())
    print(Animal.count_animals)


if __name__ == '__main__':
    main()
