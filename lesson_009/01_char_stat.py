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

    def sorting_alf(self):
        # TODO Здесь везде можно использовать sorted(self.dict_symbols.items(), key..., reverse=...)
        # TODO Тогда везде будет одинаковый тип по итогу
        # TODO я бы даже предложил сделать один метод сортировки тут, а в наследниках переопределить его
        # TODO изменяя key и reverse
        self.list_symbol = list(self.dict_symbols)
        self.list_symbol.sort()
        self.printed_value = self.list_symbol

    def sorting_alf_revers(self):
        self.list_symbol = list(self.dict_symbols)
        self.list_symbol.sort()
        self.list_symbol.reverse()
        self.printed_value = self.list_symbol

    def sorting_value(self):
        self.list_symbol = list(self.dict_symbols.items())
        self.list_symbol.sort(key=lambda i: i[1])
        self.printed_value = self.dict_symbols.items()

    def printed_result(self):
        print('+----------+-----------+')
        print('|  буква   |  частота  |')
        print('+----------+-----------+')
        # TODO вот тут странно начинается,
        # TODO сделайте в самом принте просто один вариант печати из конкретного атрибута self.printed_value например
        if isinstance(self.printed_value, list):
            for key in self.list_symbol:
                value_dict = self.dict_symbols[key]
                len_rezault_symbol = len(str(value_dict))
                len_backspace = ' ' * (8 - int(len_rezault_symbol))
                print('|   ', key, '    |', value_dict, len_backspace, '|')
                self.sum_all_symbol += self.dict_symbols[key]
        else:
            for key in self.list_symbol:
                len_rezault_symbol = len(str(key[1]))
                len_backspace = ' ' * (8 - int(len_rezault_symbol))
                print('|   ', key[0], '    |', key[1], len_backspace, '|')
                self.sum_all_symbol += key[1]

        print('+----------+-----------+')
        print('|  итого   |', self.sum_all_symbol, '  |')
        print('+----------+-----------+')

    def __str__(self):  # TODO Если ничего не задаете в этом методе - то не стоит его переопределять
        pass


inspector = Inspector()
inspector.unzip(file_name='voyna-i-mir.txt.zip')
inspector.prepare()
# inspector.sorting_alf()
# inspector.sorting_alf_revers()
inspector.sorting_value()
inspector.printed_result()

# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию

#  сделать красоту - распечатка ровными столбцами, общий блок для распечатки
