def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


test_function()
# inner_function() - будет ошибка NameError, т.к. эта функция вне зоны видимости
