from math import inf

def is_num(num):
    return isinstance(num, (int, float))


def divide(first, second):
    if not is_num(first) or not is_num(second):
        return 'Ошибка'
    elif second == 0:
        return inf
    else:
        return first / second
