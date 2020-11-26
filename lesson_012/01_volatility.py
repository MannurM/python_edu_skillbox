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
# TODO не уверен, что правильно вас понял, но как - то так...

import csv

import prepare

volatility_dict = {}
volatility_zero = []


class VolatilityObject:

    def __init__(self):
        self.dict_file = {}
        self.file_path = ''
        self.tiker_price_list = []

    def run(self, file_path):
        self.file_path = file_path
        with open(self.file_path, encoding='utf-8') as self.file:
            # TODO  выдает вот такую ошибку. почему - то ругается на генератор.
            #'Traceback (most recent call last):
            # File "C:/Users/User/PycharmProjects/python_base/lesson_012/01_volatility.py", line 123, in <module>
            # volatil.run(file_path=file_path)
            # File "C:/Users/User/PycharmProjects/python_base/lesson_012/01_volatility.py", line 85, in run
            # with open(self.file_path, encoding='utf-8') as self.file:
            # TypeError: expected str, bytes or os.PathLike object, not generator'

            reader = csv.reader(self.file, delimiter=',')
            count = 0
            for line in reader:
                if count == 0:
                    count = 1
                    continue
                self.secid, self.tiker_price = line[0], line[2]
                self.tiker_price_list.append(self.tiker_price)
            self.dict_file.update({self.secid: self.tiker_price_list})

        self.value_max = float(max(self.tiker_price_list))
        self.value_min = float(min(self.tiker_price_list))

        if self.value_max == self.value_min:
            volatility_zero.append(self.secid)

        self.half_sum = (self.value_max + self.value_min) / 2
        self.difference = (self.value_max - self.value_min)
        self.difference = round(self.difference, 4)
        self.volatility_rezult = (self.difference / self.half_sum) * 100
        self.volatility_rezult = round(self.volatility_rezult, 4)
        volatility_dict.update({self.secid: self.volatility_rezult})
        return volatility_dict, volatility_zero

        # так не пойдет, вам в целом не нужен тот класс
        # вам нужен отдельный независимый класс, который будет получать на вход путь до файла
        # и при запуске метода run - он будет счиывать файл и хранить волатильность
        # Независимыми они должны быть, т.к. далее с потоками и прцоессами доступ к общим ресурсам будет осложнен
        # поэтому сейчас я хочу чтобы вы максимально упростили свой код, чтобы понять все эти аспекты
        # которые надо будет реализовать в следующих 2 заданиях


volatil = VolatilityObject()

if __name__ == '__main__':
    file_path = prepare.file_to_path(folder_name='trades')
    print('путь к файлу есть!')
    volatil.run(file_path=file_path)
    print('Результаты')
    prepare.printed_rezult(dict_value=volatility_dict, list_zero=volatility_zero)
