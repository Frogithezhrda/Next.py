def filter_numbers(number):
    return number % 4 == 0 and number != 0


def four_dividers(number):
    return list(filter(filter_numbers, range(1, number)))


print(four_dividers(9))
