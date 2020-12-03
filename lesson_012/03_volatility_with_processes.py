# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#


import csv
from multiprocessing import Process, Queue
import prepare


class VolatilityObject(Process):

    def __init__(self, file_path, collector, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dict_file = {}
        self.file_path = file_path
        self.tiker_price_list = []
        self.secid = None
        self.volatility_rezult = 0
        self.file = None
        self.collector = collector

    def run(self):
        with open(self.file_path, encoding='utf-8') as self.file:
            reader = csv.reader(self.file, delimiter=',')
            count = 0
            for line in reader:
                if count == 0:
                    count = 1
                    continue
                self.secid, tiker_price = line[0], line[2]
                self.tiker_price_list.append(float(tiker_price))

        value_max = max(self.tiker_price_list)
        value_min = min(self.tiker_price_list)
        if value_max == value_min:
            self.volatility_rezult = 0
        else:
            half_sum = (value_max + value_min) / 2
            difference = value_max - value_min
            self.volatility_rezult = (difference / half_sum) * 100
            self.volatility_rezult = round(self.volatility_rezult, 2)
        self.collector.put([self.secid, self.volatility_rezult])


if __name__ == '__main__':
    folder_name = 'trades'
    collector = Queue()
    volatils = [VolatilityObject(file_path=file_path, collector=collector)
                for file_path in prepare.file_to_path(folder_name=folder_name)]
    volatility_dict = {}
    volatility_zero = []
    for volatil in volatils:
        volatil.start()
        # print(volatil)
    for volatil in volatils:
        volatil.join()
        # print(volatil)
        data_queue = collector.get()
        if data_queue[1] == 0:
            volatility_zero.append(data_queue[0])
        else:
            volatility_dict.update({data_queue[0]: data_queue[1]})

    prepare.printed_rezult(dict_value=volatility_dict, list_zero=volatility_zero)
# А с трубами не получилось (
# TODO текущий код тоже не работает, вылезает ошибка:
# Traceback (most recent call last):
#   File "C:/skillbox/python_base_zajdullin_mannur/lesson_012/03_volatility_with_processes.py", line 66, in <module>
#     for file_path in prepare.file_to_path(folder_name=folder_name)]
# TypeError: file_to_path() missing 1 required positional argument: 'list_file_in_folder'
# TODO а с трубами в чём была проблема? можете создать ещё один файл и показать вариант с ними?
