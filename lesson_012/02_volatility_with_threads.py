# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
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

import csv
import prepare
from threading import Thread


class VolatilityObject(Thread):
    def __init__(self, file_path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dict_file = {}
        self.file_path = file_path
        self.tiker_price_list = []
        self.secid = None
        self.volatility_rezult = 0
        self.file = None

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
        return self.secid, self.volatility_rezult


if __name__ == '__main__':
    file_path_list = [VolatilityObject(file_path=file_path)for file_path in prepare.file_to_path(folder_name='trades')]
    list_volatil = []
    for volatil in file_path_list:
        volatil.start()
        list_volatil.append(volatil)

    volatility_dict = {}
    volatility_zero = []
    for volatil in list_volatil:
        volatil.join()

        if volatil.volatility_rezult == 0:
            volatility_zero.append(volatil.secid)
            continue
        else:
            volatility_dict.update({volatil.secid: volatil.volatility_rezult})

    prepare.printed_rezult(dict_value=volatility_dict, list_zero=volatility_zero)
#зачёт!