calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(my_str: str):
    count_calls()
    my_tuple = (len(my_str), my_str.upper(), my_str.lower())
    return my_tuple


def is_contains(my_str: str, my_list: list):
    count_calls()
    for i in my_list:
        if my_str.lower() == i.lower():
            return True
    return False


list1 = ['gg', '123', 'papA', 'mama']
print(is_contains('Gosha', list1))
print(is_contains('pApa', list1))
print(string_info('Urban'))
print(string_info('University'))

print(calls)
