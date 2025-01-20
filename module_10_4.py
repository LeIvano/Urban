import threading
import queue
import random
import time


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        wait_time = random.randint(3, 10)
        time.sleep(wait_time)


class Cafe:
    def __init__(self, *args):
        self.queue = queue.Queue()
        self.tables = list(args)

    def guest_arrival(self, *guests):
        for guest in guests:
            was_sitting = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел за стол номер {table.number}')
                    was_sitting = True
                    break

            if not was_sitting:
                print(f'{guest.name} в очереди')
                self.queue.put(guest)

    def discuss_guests(self):
        is_person_in = False
        while not self.queue.empty() or is_person_in:
            is_person_in = False
            for table in self.tables:
                if table.guest is None:
                    continue
                if not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None

                    if not self.queue.empty():
                        table.guest = self.queue.get()
                        table.guest.start()
                        print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        is_person_in = True
                else:
                    is_person_in = True


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
