import file1


class BirthdayCard(file1.GreetingCard):
    def __init__(self, sender_age=0):
        super().__init__()
        self._sender_age = sender_age
    def greeting_msg(self):
        super().greeting_msg()
        print("Age " + str(self._sender_age), "Happy Birthday")
