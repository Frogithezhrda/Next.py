class Animal:

    def __init__(self):
        self.name = ""
        self.age = 0

    def get_age(self):
        return self.age

    def birthday(self):
        self.age = self.age + 1

    def print_animal_age(self):
        print(self.age)


def main():
    frog = Animal()
    shark = Animal()
    frog.birthday()
    shark.print_animal_age()
    frog.print_animal_age()


if __name__ == '__main__':
    main()
