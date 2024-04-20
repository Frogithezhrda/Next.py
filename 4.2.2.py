def parse_ranges(ranges_string):
    seperated_fixed = []
    seperated = (letter.split('-') for letter in ranges_string.split(','))
    for start, stop in seperated:
        for num in range(int(start), int(stop)+1):
            seperated_fixed.append(num)
    return seperated_fixed


print(parse_ranges("1-2,4-4,8-10"))
