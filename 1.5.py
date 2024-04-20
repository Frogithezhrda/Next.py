# with open("names.txt", "r") as file:
#    print(max(file.read().split("\n")))
# import functools
# with open("names.txt") as file:
#    print(functools.reduce(lambda x, y: x + y, (len(name) for name in file.read().split("\n"))))
# min_length = len(min(open("names.txt").read().split("\n"), key=len))
# print(*[name for name in open("names.txt").read().split("\n") if len(name) == min_length])
# names = open("names.txt").read().split("\n")
# for name in names:
#    print(str(len(name)))
# length = int(input("Name Length:"))
# print('\n'.join([name for name in open("names.txt").read().split("\n") if len(name) == length]))
