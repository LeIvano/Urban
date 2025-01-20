import threading
import time
from random import randint


class Bank:
    def __init__(self, balance=0, lock=threading.Lock()):
        self.balance = balance
        self.lock = lock

    def deposit(self):
        for _ in range(100):
            adding_value = randint(50, 501)
            self.balance += adding_value

            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

            print(f'Пополнение: {adding_value}. Баланс: {self.balance}')

            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            take_value = randint(50, 501)
            print(f'Запрос на {take_value}')

            if take_value <= self.balance:
                self.balance -= take_value
                print(f'Снятие: {take_value}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()

            time.sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
