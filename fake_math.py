def is_num(num):
    return isinstance(num, (int, float))

def divide(first,second):
    if not is_num(first) or not is_num(second) or second == 0:
        return 'Ошибка'
    else:
        return first / second
