#1
print('#1')
def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)


print_params()
print_params(5)
print_params(10,'mama')
print_params(25, 'papa', False)

print_params(b = 25)
print_params(c = [1,2,3])
#Вызовы работают, но есть варнинги из-за умной типизации ide

#2
print('\n#2')
values_list = [25, 'papa', False]
values_dict = {'a': 50, 'b': 'gg', 'c':True}
print_params(*values_list)
print_params(**values_dict)

#3
print('\n#3')
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)

