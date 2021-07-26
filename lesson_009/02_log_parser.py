# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате

# 1) прочитать файл
# 2) пересчитать события, найти все NOK,  сравнить минуты
# 3) Создать файл результата, открыть файл, записать данные, закрыть файл
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

from collections import defaultdict


class Reader:

    def __init__(self):
        self.file = None
        self.file_name = None
        self.file_name_result = None
        self.dict_symbols = defaultdict(int)
        self.end_segment = 17

    def __str__(self):
        pass

    def create_result_file(self):  # Создание результирующего файла, открытие файла, добавление результатов, закрытие
        self.file_name_result = 'result_' + self.file_name
        self.file = open(self.file_name_result, mode='w')
        for key, value in self.dict_symbols.items():
            key_value = key + ' ' + str(value) + '\n'
            self.file.write(key_value)
        self.file.close()

    def open_file(self):  # открытие  файла с результатами
        self.file_name = self.file_name_result
        self.file = open(self.file_name, mode='r', encoding='utf8')
        for line in self.file:
            print(line)
        self.file.close()

    def prepare(self, file_name):  # подготовка и расчеты
        self.file_name = file_name
        self.file = open(self.file_name, mode='r', encoding='utf8')
        for line in self.file:
            if line[-4:-3] == 'N':
                different_symbol = line[1:self.end_segment]
                self.dict_symbols[different_symbol] += 1
        self.file.close()

    def run_programm(self, file_name):
        self.prepare(file_name)
        self.create_result_file()
        self.open_file()


class SorteredHour(Reader):

    def __init__(self):
        super().__init__()
        self.end_segment = 14


class SorteredDay(Reader):

    def __init__(self):
        super().__init__()
        self.end_segment = 12


class SorteredMount(Reader):

    def __init__(self):
        super().__init__()
        self.end_segment = 8


class SorteredYear(Reader):

    def __init__(self):
        super().__init__()
        self.end_segment = 5


reader = Reader()
# reader.run_programm(file_name='events.txt')

# reader = SorteredYear()
# reader = SorteredDay()
reader.run_programm(file_name='events.txt')
# reader = SorteredHour()
# reader = SorteredMount()


#  И надо реализовать вторую часть с минимумом дублирования кода

# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
#зачёт!