import itertools

dollars = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
counter = 0
for dollar in range(len(dollars)):
    for money in set(itertools.combinations(dollars, dollar)):
        if sum(money) == 100:
            counter += 1

print(counter)
