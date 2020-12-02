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


import os
from multiprocessing import Process, Pipe, Queue
from queue import Empty


import csv

import prepare


class VolatilityObject(Process):

    def __init__(self, file_path, conn, *args, **kwargs):
        super(Process).__init__(*args, **kwargs)
        self.dict_file = {}
        self.file_path = file_path
        self.tiker_price_list = []
        # secid = None
        # volatility_rezult = 0
        self.file = None
        self.conn = conn

    def run(self):
        with open(self.file_path, encoding='utf-8') as self.file:
            reader = csv.reader(self.file, delimiter=',')
            count = 0
            for line in reader:
                if count == 0:
                    count = 1
                    continue
                secid, tiker_price = line[0], line[2]
                self.tiker_price_list.append(float(tiker_price))

        value_max = max(self.tiker_price_list)
        value_min = min(self.tiker_price_list)
        if value_max == value_min:
            volatility_rezult = 0
        else:
            half_sum = (value_max + value_min) / 2
            difference = value_max - value_min
            volatility_rezult = (difference / half_sum) * 100
            volatility_rezult = round(volatility_rezult, 2)
        self.conn.send(secid, volatility_rezult)
        self.conn.close()
        # return self.secid, self.volatility_rezult

# TODO Я куда-то не в ту степь уехал...))
# TODO Вопросы: в каком месте разбивать на процессы
# TODO

if __name__ == '__main__':
    folder_name = 'trades'
    file_in_folder = os.listdir(folder_name)
    len_folder = len(file_in_folder)
    count_file = int(round(len_folder / 2, 0))
    # print(count_file)
    list_file_folder = list(file_in_folder)

    list_file_folder_1 = list_file_folder[:count_file]
    list_file_folder_2 = list_file_folder[count_file + 1:]
    # print(list_file_folder_1)
    # print(list_file_folder_2)

    list_volatil = []
    volatility_dict = {}
    volatility_zero = []
    pipes = []
    for file in list_file_folder:
        parent_conn, child_conn = Pipe()
        target_1 = [VolatilityObject(file_path=file_path, conn=child_conn)for file_path in
                            prepare.file_to_path(folder_name=folder_name, list_file_in_folder=list_file_folder_1)]
        volatil_1 = Process(group=None, target=target_1)

        target_2 = [VolatilityObject(file_path=file_path, conn=child_conn)for file_path in
                            prepare.file_to_path(folder_name=folder_name, list_file_in_folder=list_file_folder_2)]
        volatil_2 = Process(group=None, target=target_2)

        print(volatil_1, volatil_2)
        volatil_1.start()
        volatil_2.start()
        print('1')
        for conn in pipes:

            secid, volality_rezult = parent_conn.recv()
            print(secid, volality_rezult)
        volatil_1.join()
        volatil_2.join()

        if volatil_1.volatility_rezult == 0:
            volatility_zero.append(volatil_1.secid)
            continue
        elif volatil_2.volatility_rezult == 0:
            volatility_zero.append(volatil_2.secid)
            continue
        else:
            volatility_dict.update({volatil_1.secid: volatil_1.volatility_rezult})
            volatility_dict.update({volatil_2.secid: volatil_2.volatility_rezult})

        prepare.printed_rezult(dict_value=volatility_dict, list_zero=volatility_zero)


