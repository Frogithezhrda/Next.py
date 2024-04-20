import functools


def sum_of_digits(number):
    return functools.reduce(func, list(map(int, str(number))))


def func(number, number2):
    return number + number2

print(sum_of_digits(104))
