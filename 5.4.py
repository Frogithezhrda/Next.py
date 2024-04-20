def check_id_valid(id_number):
    id_list = []
    for number in range(len(str(id_number))):
        if number % 2 == 1:
            id_list.append(str(int(str(id_number)[number]) * 2))
        else:
            id_list.append((str(int(str(id_number)[number]))))
    for ids in range(len(id_list)):
        if int(id_list[ids]) > 9:
            id_list[ids] = str(int(id_list[ids][:1]) + int(id_list[ids][1:2]))
    if sum(int(digit) for digit in id_list) % 10 == 0:
        return True
    return False


def id_generator(id_number=100000000):
    while True:
        try:
            if id_number == 999999999:
                raise StopIteration
            elif check_id_valid(id_number):
                yield id_number
            id_number += 1
        except Exception as exception:
            print(exception)


class IDIterator:
    def __init__(self, id_num=100000000):
        self._id = id_num

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self._id == 999999999:
                raise StopIteration
            elif check_id_valid(self._id):
                valid_id = self._id
                self._id += 1
                return valid_id
            else:
                self._id += 1


def main():
    id_input = int(input("Enter ID: "))
    gen_or_iter = input("Generator or Iterator? (gen/it)? ")
    if gen_or_iter == "it":
        id_user_iter = IDIterator(id_input)
        for _ in range(10):
            print(next(id_user_iter))
    elif gen_or_iter == "gen":
        gen = id_generator(id_input)
        for _ in range(10):
            print(next(gen))


if __name__ == '__main__':
    main()
