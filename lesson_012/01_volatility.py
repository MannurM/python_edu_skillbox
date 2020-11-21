# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от полусуммы крайних значений цены за торговую сессию:
#   полусумма = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / полусумма) * 100%
# Например для бумаги №1:
#   half_sum = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / half_sum) * 100 = 8.7%
# Для бумаги №2:
#   half_sum = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / half_sum) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
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
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
import csv
import os


# import operator


class Volatility:

    def __init__(self):  # <сохранение параметров>
        self.dir_name = None
        self.secid = None  # имя тикера
        self.tiker_time = None  # время тикера
        self.tiker_quantity = None  # количество проданного
        self.tiker_price = []
        self.file_in_folder = 0  # количества файлов в исходной папке
        self.volatility_rezult = 0
        self.volatility_max = []
        self.volatility_min = []
        self.volatility_dict = {}
        self.volatility_zero = []
        self.tiker_price_list = []  # список значений из файла
        self.half_sum = 0  # полусумма
        self.difference = 0  # разность макс и мин
        self.value_max = 0
        self.value_min = 0
        self.dict_file = {}
        self.key = None
        # self.param_dir = param_dir  # Путь до папки с файлами?

    def run(self, dir_name):  # <обработка данных>
        self.dir_name = dir_name
        self.file_in_folder = os.listdir(self.dir_name)
        path = os.getcwd() + '\\' + self.dir_name
        path = os.path.normpath(path)

        for file in self.file_in_folder:
            print(file)
            file = path + '\\' + file
            self.prepare(file)
            self.tiker_price_list = self.dict_file[self.secid]
            sorted(self.tiker_price_list)
            self.value_max = float(max(self.tiker_price_list))
            self.value_min = float(min(self.tiker_price_list))
            if self.value_max == self.value_min:
                self.volatility_zero.append(self.secid)
            self.half_sum = (self.value_max + self.value_min) / 2
            self.difference = (self.value_max - self.value_min)
            self.difference = round(self.difference, 4)
            self.volatility_rezult = (self.difference / self.half_sum) * 100
            self.volatility_rezult = round(self.volatility_rezult, 4)
            self.volatility_dict.update({self.secid: self.volatility_rezult})
            print('____________', self.value_max, self.value_min, self.half_sum, self.difference,
                  self.volatility_rezult)

            self.tiker_price_list = []
            self.value_max = 0
            self.value_min = 0
            self.volatility_rezult = 0
            self.half_sum = 0
            self.difference = 0

        # print(self.volatility_dict)

        # self.volatility_max = list(self.volatility_dict.items(), key=operator.itemgetter(1))
        for i, v in self.volatility_dict.items():
            self.volatility_max.append(v)
        self.volatility_min = self.volatility_max
        #  Вывод на консоль
        self.volatility_max.sort(reverse=True)
        print('Максимальная волатильность:')
        for i in range(3):
            self.get_value(dic=self.volatility_dict, value=self.volatility_max[i])
            print(self.key, self.volatility_max[i])

        self.volatility_min.sort()
        print('Минимальная волатильность:')
        for i in range(3):
            self.get_value(dic=self.volatility_dict, value=self.volatility_min[i])
            print(self.key, self.volatility_min[i])

        self.volatility_zero.sort()
        print('Нулевая волатильность:')
        print(self.volatility_zero)

        # Запустил препаре
        # получил словарь из препаре
        # взял имя тикера
        # нашел макс и мин, сравнил если одинаковые то имя тикера добавил в список зеро
        # получил полусумму, получил разность
        # высчитал волатильность - добавил в новый словарь? или заменил значение в словаре из препаре? или
        # создал 2 списка - список тикеров и список значений волатильности - как связать два списка?
        # или добавил попарные значения в списки или в defaultdict 1 и 2?
        # сравнил значения списке нашел мин, макс - сет негодится он удалит одинаковые значения

    def prepare(self, file):  # предобработка данных
        with open(file, newline='', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            count = 0
            for line in reader:
                if count == 0:
                    count = 1
                    continue
                self.secid, self.tiker_price = line[0], line[2]
                self.tiker_price_list.append(self.tiker_price)
            # return self.secid, self.tiker_price_list

            self.dict_file.update({self.secid: self.tiker_price_list})
        return self.dict_file

        # посчитать количество файлов в исходной папке
        # открыть файл,
        # прочитать все строки построчно, взять secid и price и добавить в словарь
        # dict(self.secid = name, self.tiker_price = self.tiker_price.append(price)) (как вариант значения это список)
        # self.dict_file.update(self.tiker_price, self.secid)
        # dict.fromkeys(seq[, value])
        # закрыть файл
        # вернуть словарь (имя : список значений)

    def get_value(self, dic, value):
        for self.key in dic:
            if dic[self.key] == value:
                return self.key


volatil = Volatility()

volatil.run(dir_name='trades')
