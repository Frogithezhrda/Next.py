class UnderAge(Exception):
    def __str__(self):
        return "The Age is not legal you are %s in a few years you can go to ido's birthday!" % self._age

    def __init__(self, age):
        self._age = age

    def get_arg(self):
        return self._age


def send_invitation(name, age):
    if int(age) < 18:
        raise UnderAge(age)
    else:
        print("You should send an invite to " + name)


send_invitation("shilat", 20)
