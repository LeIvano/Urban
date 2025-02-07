import asyncio


async def start_strongman(name, power):
    """
    Функция имитации соревнований по поднятию шаров Атласа
    :param name: Имя силача
    :param power: Подъёмная мощность
    """

    print(f'Силач {name} начал соревнования.')
    for ball in range(1, 6):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {ball} шар')

    print(f'Силач {name} закончил соревнования.')


async def start_tournament(**kwargs):
    """
    Соревнование силачей
    :param kwargs: Участники соревнования
    """
    tasks_array = list()
    for key, value in kwargs.items():
        tasks_array.append(asyncio.create_task(start_strongman(key, value)))

    for task in tasks_array:
        await task


asyncio.run(start_tournament(Ivan=30, Igor=10, Richard=29))
