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
'voyna-i-mir.txt'

class Inspector:

    def __init__(self, file_name):
        self.dict_symbols = defaultdict(int)
        self.file_name = file_name
        self.sum_all_symbol = 0
    # TODO выдает ошибку при распаковке
    # def unzip(self):
    #     zfile = zipfile.ZipFile(self.file_name, 'r')
    #     for filename in zfile.namelist():
    #         zfile.extract(filename)
    #     self.file_name = filename



    def prepare(self):
        with open(self.file_name, mode='r', encoding='cp1251') as file:
            for line in file:
                line = line[:-1]
                for symbol in line:
                    if not symbol.isalpha():
                        continue
                    if not line:
                        continue
                    self.dict_symbols[symbol] += 1

    def collating(self):
        pass


    def __str__(self):
        print('+----------+-----------+')
        print('|  буква   |  частота  |')
        print('+----------+-----------+')
        for key in self.dict_symbols:
            value_dict = self.dict_symbols[key]
            print('| ', key, '    |    ', value_dict, '    |')
            self.sum_all_symbol += value_dict
        print('+----------+-----------+')
        print('|  итого   |', self.sum_all_symbol, ' |')
        print('+----------+-----------+')
        return

# inspector = Inspector(file_name='voyna-i-mir.txt.zip')
inspector = Inspector(file_name='voyna-i-mir.txt')
inspector.prepare()

print(inspector)


# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
