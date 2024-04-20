def intersection(list1, list2):
    return list(set([item for item in list1 for item2 in list2 if item == item2]))


print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))
