# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4
import zipfile
from collections import defaultdict


class Inspector:

    def __init__(self):
        self.sorted_key = None
        self.dict_symbols = defaultdict(int)
        self.file_name = None
        self.sum_all_symbol = 0
        self.counter = None
        self.list_symbol = []
        self.printed_value = None

    def unzip(self, file_name):
        self.file_name = file_name
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            self.file_name = zfile.extract(filename)
        return

    def prepare(self):
        with open(self.file_name, mode='r', encoding='cp1251') as file:
            for line in file:
                line = line[:-1]
                for symbol in line:
                    if symbol.isalpha():
                        self.dict_symbols[symbol] += 1
                self.sum_all_symbol += self.dict_symbols[symbol]

    def sorting_value(self, key):
        self.list_symbol = sorted(self.dict_symbols.items(), key=key().sorted_key, reverse=False)
        self.printed_value = self.list_symbol

    def printed_result(self):
        print('+----------+-----------+')
        print('|  буква   |  частота  |')
        print('+----------+-----------+')

        for key in self.printed_value:
            if key[0].isalpha():
                len_rezault_symbol = len(str(key[1]))
                len_backspace = ' ' * (8 - int(len_rezault_symbol))
                print('|   ', key[0], '    |', key[1], len_backspace, '|')

        print('+----------+-----------+')
        print('|  итого   |', self.sum_all_symbol, '  |')
        print('+----------+-----------+')
    # TODO нужно тут сделать один общий метод, который вызовет остальные в правильном порядке


class Sorting(Inspector):

    def __init__(self):
        super().__init__()
        self.list_symbol = None
        self.printed_value = None
        self.sorted_key = None
        self.sorted_reverse = None


class SortingAlf(Sorting):

    def __init__(self):
        super().__init__()
        self.sorted_key = lambda i: i[0]
        self.sorted_reverse = False


class SortingAlfRevers(Sorting):

    def __init__(self):
        super(Sorting, self).__init__()
        self.sorted_key = lambda i: i[0]
        self.sorted_reverse = True  # тут видимо True должен быть


class SortingValue(Sorting):
    def __init__(self):
        super(Sorting, self).__init__()
        self.sorted_key = lambda i: i[1]
        self.sorted_reverse = False


inspector = Inspector()
inspector.unzip(file_name='voyna-i-mir.txt.zip')
inspector.prepare()
inspector.sorting_value(key=SortingAlf)  # SortingAlfRevers, SortingAlf
inspector.printed_result()


# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию

#  сделать красоту - распечатка ровными столбцами, общий блок для распечатки
