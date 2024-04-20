class BigThing:
    def __init__(self, variable):
        self.variable = variable

    def size(self):
        if type(self.variable) == int:
            return self.variable
        else:
            return len(self.variable)


class BigCat(BigThing):
    def __init__(self, name, weight):
        self.weight = weight
        self.name = name

    def size(self):
        if 15 <= self.weight < 20:
            return "Fat"
        elif 20 <= self.weight:
            return "Very Fat"
        else:
            return "ok"


def main():
    cutie = BigCat("mitzy", 15)
    print(cutie.size())


if __name__ == '__main__':
    main()
