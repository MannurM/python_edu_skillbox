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

class Reader:

    def __init__(self):
        self.file = None
        self.file_name = None
        self.file_name_result = None
        self.file_new = []
        self.count = 0
        self.a = 0
        self.b = 0

    def __str__(self):
        pass

    def create_result_file(self):  # Создание результирующего файла, открытие файла, добавление результатов, закрытие
        self.file_name_result = self.file_name + '_result'
        self.file = open(self.file_name_result, mode='w')

        for index in range(len(self.file_new)):
            self.file.write(self.file_new[index])
        self.file.close()

    def open_file(self, file_name):  # открытие исходного фалв
        self.file_name = file_name
        with open(self.file_name, mode='r', encoding='utf8') as self.file:
            for line in self.file:
                pass
            print('file open!')

    def prepare(self):  # расчеты
        with open(self.file_name, mode='r', encoding='utf8') as self.file:
            for line in self.file:
                if line[-4:-3] == 'N':
                    line = line[1:17]
                    self.file_new.append(line)
                    # self.file_new[line] =
                    self.file_new.sort()
            print(self.file_new)
            for index in range(len(self.file_new) - 1):
                self.a = self.file_new[index][:16]
                self.b = self.file_new[index + 1][:16]
                if self.a == self.b:
                    # print(self.a, self.b)
                    self.count += 1
                else:
                    # print(self.file_new[index] + str(self.count))
                    self.file_new[index] += '---' + str(self.count+1) + '\n'
                    self.count = 0

    def sorted_result(self):
        pass


reader = Reader()
reader.open_file(file_name='events.txt')
reader.prepare()
reader.create_result_file()

# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
