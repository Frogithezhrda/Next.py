numbers = iter(list(range(1, 103)))
for i in numbers:
    next(numbers)
    print(next(numbers))
