from itertools import combinations


def all_variants(text):
    # Генерация всех длин от 1 до длины текста
    for length in range(1, len(text) + 1):
        # Генерация всех комбинаций указанной длины
        for combination in combinations(text, length):
            yield ''.join(combination)


a = all_variants("abc")
for i in a:
    print(i)
