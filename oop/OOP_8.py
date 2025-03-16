from datetime import datetime
import pytz
from colorama import init, Fore, Style
init()

GREEN = Fore.GREEN
WHITE = Fore.WHITE
RED = Fore.RED

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self.history = []

    @staticmethod
    def _get_current_time():
        return pytz.utc.localize(datetime.utcnow())

    def deposit(self, amount):
        self.__balance += amount
        self.show_balance()
        self.history.append([amount, self._get_current_time()])

    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            print(f'Вы потратили {amount}')
            self.show_balance()
            self.history.append([-amount, self._get_current_time()])
        else:
            print("Недостаточно денег")
            self.show_balance()

    def show_balance(self):
        print(f'Баланс {self.__balance}')

    def show_history(self):
        for amount, date in self.history:
            if amount > 0:
                transaction = 'deposit'
                color = GREEN
            else:
                transaction = 'withdraw'
                color = RED
            print(f'{color}{amount} {WHITE}{transaction} {date.astimezone()}{Style.RESET_ALL}')


a = Account("Kirill", 0)


a.deposit(100)
a.withdraw(21)
a.show_history()

