from file1 import GreetingCard
from file2 import BirthdayCard

def main():
    GreetingCard().greeting_msg()
    BirthdayCard(12).greeting_msg()
if __name__ == '__main__':
    main()
