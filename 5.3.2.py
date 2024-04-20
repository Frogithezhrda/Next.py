class MusicNotes:
    def __init__(self):
        self.lst = [55, 61.74, 65.41, 73.42, 82.41, 87.31, 98]
        self.fixed_list = self.lst.copy()
        for item in self.lst:
            self.fixed_list.append((item * 2))
        for n in range(1, 4):
            for item in self.lst:
                self.fixed_list.append((item * 2) * 2 ** n)
        self.lst_index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.lst_index >= len(self.fixed_list) - 1:
            raise StopIteration
        self.lst_index += 1
        return self.fixed_list[self.lst_index]


notes_iter = iter(MusicNotes())


for freq in notes_iter:
    print(freq)
