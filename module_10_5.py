from multiprocessing import Pool
import time


def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        for line in f:
            all_data.append(line)


if __name__ == '__main__':

    filenames = [f'Files/file {number}.txt' for number in range(1, 5)]

    time_begin = time.time()
    # Линейный вызов
    # for filename in filenames:
    #    read_info(filename)

    # Многопроцессный
    with Pool(4) as p:
        p.map(read_info, filenames)

    print(time.time() - time_begin)
