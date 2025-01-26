import inspect
from pprint import pprint


class MyClass():
    def __init__(self):
        self.name = "Ivan"
        self.age = "20"
        self.height = 180

    def print_age(self):
        print(f'My age is {self.age}')

    def get_height(self):
        return self.height


def introspection_info(obj):
    dictonary = dict()

    dictonary['type'] = str(type(obj)).split("'")[1]
    dictonary['attributes'] = dir(obj)

    methods = inspect.getmembers(sth, predicate=inspect.ismethod)
    dictonary['methods'] = [method[0] for method in methods]

    dictonary['module'] = str(inspect.getmodule(obj)).split("'")[1]

    return dictonary


if __name__ == "__main__":
    sth = MyClass()
    result = introspection_info(sth)

    pprint(result)