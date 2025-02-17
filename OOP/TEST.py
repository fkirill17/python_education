import time


class Account:
    def __init__(self, name, deposit):
        self.name = name
        self.deposit = deposit
        self.history = []

    def deposit_up(self, amount):
        self.deposit += amount
        self.history.append(f"Вы пополнили счет на {amount}. Время: {self.current_time()}")
        self.show_balance()

    def deposit_down(self, amount):
        if self.deposit >= amount:
            self.deposit -= amount
            self.history.append(f"Вы сняли со счета {amount}. Время: {self.current_time()}")
            self.show_balance()

    def show_balance(self):
        print(self.deposit)

    def show_history(self):
        print(self.history)

    @staticmethod
    def current_time():
        return time.time()


a = Account("Kirill", 160000)

a.deposit_up(70000)

a.show_history()
