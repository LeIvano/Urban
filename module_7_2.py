def custom_write(file_name, strings):
    count = 1
    dictionary = {}
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
        my_tuple = (count, file.tell())
        file.write(string)
        file.write('\n')
        dictionary[my_tuple] = string
        count += 1

    return dictionary


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
