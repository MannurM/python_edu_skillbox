# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>  # Итератор или генератор? выбирайте что вам более понятно
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

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

reader.run_programm(file_name='events.txt')
# TODO здесь пока нету ни генератора, ни итератора
# TODO Я бы кстати рекомендовал делать это задание через функцию-генератор
# TODO Нужно чтобы при обращении к ней генератор читал файл ровно до следующей минуты (не полностью!)
# TODO и возвращал результат за текущую минуту через Yield