class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)


    def get_all_words(self):
        all_words = dict()
        for file_name in self.file_names:
            words = list()
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for char in [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']:
                        line = "".join(line.split(char))
                    line_words = line.split(' ')
                    for word in line_words:
                        words.append(word)

            all_words[file_name] = words

        return all_words

    def find(self, word):
        return_dict = dict()
        word = word.lower()
        all_words = self.get_all_words()
        for key, value in all_words.items():
            if word in value:
                return_dict[key] = value.index(word) + 1
                return return_dict

        return return_dict

    def count(self, word):
        return_dict = dict()
        word = word.lower()
        all_words = self.get_all_words()
        for key, value in all_words.items():
            if word in value:
                return_dict[key] = value.count(word)
                return return_dict

        return return_dict


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
