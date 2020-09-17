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

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def prepare(self):
        # with open(self.file_name, mode='r') as file:  # , encoding='utf-8'  , encoding='cp1251'
        # TODO я пробовал оба варианта, может начинать считывать побайтно как-то?
        with open(self.file_name, mode='r', encoding='cp1251') as file:
            for line in file:
                line = line[:-1]
                for symbol in line:
                    if symbol.isalpha():
                        self.dict_symbols[symbol] += 1

    # TODO Traceback (most recent call last):
    # TODO  File "C:/Users/User/PycharmProjects/python_base/lesson_009/01_char_stat.py", line 75, in <module>
    # TODO inspector.prepare()
    # TODO File "C:/Users/User/PycharmProjects/python_base/lesson_009/01_char_stat.py", line 49, in prepare
    # TODO for line in file:
    # TODO File "C:\Program Files\Python37\Lib\encodings\cp1251.py", line 23, in decode
    # TODO  return codecs.charmap_decode(input,self.errors,decoding_table)[0]
    # TODO UnicodeDecodeError: 'charmap' codec can't decode byte 0x98 in position 141: character maps to <undefined>

    def collating(self):
        pass

    def printed_result(self):
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

    def __str__(self):
        pass


inspector = Inspector(file_name='voyna-i-mir.txt.zip') # файл расположен в одной папке с программой 01_char_stat
inspector.prepare()
inspector.printed_result()

# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
