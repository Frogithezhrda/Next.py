import string


class UsernameTooShort(Exception):
    def __str__(self):
        return "User Name Too Short!"


class UsernameTooLong(Exception):
    def __str__(self):
        return "User Name Too Long!"


class PasswordTooShort(Exception):
    def __str__(self):
        return "Password Too Short!"


class PasswordTooLong(Exception):
    def __str__(self):
        return "Password Too Long!"


class UsernameContainsIllegalCharacter(Exception):
    def __str__(self):
        return f"User Name Contains Illegal Characters! The Char {self.char} , at index {self.username.find(self.char) + 1}"

    def __init__(self, char, username):
        self.char = char
        self.username = username


class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "Password Missing Essential Chars!"


class Uppercase(PasswordMissingCharacter):
    def __str__(self):
        return f"Missing Uppercase Letters!"


class Lowercase(PasswordMissingCharacter):
    def __str__(self):
        return f"Missing Lowercase Letters!"


class Special(PasswordMissingCharacter):
    def __str__(self):
        return f"Missing Special Letters!"


class Digit(PasswordMissingCharacter):
    def __str__(self):
        return f"Missing A Digit!"


def check_input(username, password):
    # user name check
    try:
        for char in username:
            if not char.isalnum() and char != "_":
                raise UsernameContainsIllegalCharacter(char, username)
            elif 3 > len(username):
                raise UsernameTooShort
            elif 16 < len(username):
                raise UsernameTooLong
    except Exception as exception:
        return exception
        # Password check
    try:
        if not any(char in string.punctuation for char in password):
            raise Special
        elif not any(char in string.ascii_lowercase for char in password):
            raise Lowercase
        elif not any(char in string.ascii_uppercase for char in password):
            raise Uppercase
        elif not any(char in string.digits for char in password):
            raise Digit
        elif len(password) < 8:
            raise PasswordTooShort
        elif len(password) > 40:
            raise PasswordTooLong
        else:
            return "OK!"
    except Exception as exception:
        return exception


def main():
    username = input("Username: ")
    password = input("Password: ")
    print(check_input(username, password))


if __name__ == '__main__':
    main()
