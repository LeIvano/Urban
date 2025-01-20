import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')

        enemies_count = 100
        days_count = 0

        while True:
            time.sleep(1)
            days_count += 1
            enemies_count -= self.power
            if enemies_count <= 0:
                break
            print(f'{self.name} сражается {days_count} дней, осталось {enemies_count} воинов.')

        print(f'{self.name} одержал победу спустя {days_count} дней(дня)!')


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print("Все битвы закончились")