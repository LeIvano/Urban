import pandas as pd
import numpy as np
import random


def random_file(name: str, count_els: int):
    if count_els <= 0:
        return

    with open(name, 'w') as file:
        for _ in range(count_els):
            file.write(str(random.randint(0, count_els + 1)))
            file.write('\n')


def test_pandas():
    print("PANDAS")

    name = 'for_test.txt'
    random_file(name, 100)

    with open(name, 'r') as file:
        data = [int(x) for x in file]

    s = pd.Series(data)
    print('-----------------')
    print(s.describe())
    print('-----------------')
    print(s.T)
    print('-----------------')
    print(s.array)
    print('-----------------')


def test_numpy():
    print("NUMPY")

    array = np.arange(2, 9, 2)
    print('-----------------')
    print(array)
    print('-----------------')
    print(array[array<5])
    print('-----------------')
    ones = np.ones(4, dtype=int)
    array = array + ones
    print(array)
    print('-----------------')


if __name__ == '__main__':
    test_pandas()
    test_numpy()

