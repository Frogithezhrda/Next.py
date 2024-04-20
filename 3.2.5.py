def read_file(file_name):
    """i can add it to a string and return it but i am lazy"""
    try:
        print("__CONTENT_START__")
        file = open(file_name)
    except IOError:
        print("__NO_SUCH_FILE__")
    else:
        print(file.read())
    finally:
        print("__CONTENT_END__")
        return ""


print(read_file("names.txt"))
