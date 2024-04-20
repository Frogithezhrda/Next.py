def combine_coins(coin, numbers):
    return ''.join([coin + str(number) + ", " for number in numbers])[:-2]


print(combine_coins('$', range(10)))
