def is_funny(string):
    return not bool([True for char in string if char != 'h' and char != 'a'])


print(is_funny("hahahahaha"))
