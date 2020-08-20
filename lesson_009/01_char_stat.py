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
from collections import Counter


class Inspector:
    pass


# z = zipfile.ZipFile('python_snippets/voyna-i-mir.txt.zip', 'r')
# voyna_i_mir = z.extractall('C:/users/user/PycharmProjects/python_base/lesson_009')  # voyna-i-mir.txt.zip
# z.close()
dict_symbols = {}
dict_symbols_all = {}
list_symbols = []
file_name = 'voyna-i-mir.txt'
value_new = 0
sum_all_symbol = 0
dict_symbols_old = {}
# file = open('voyna-i-mir.txt', mode='r')
# # file_content = file.read()
# # file.close()
# # pprint(file_content)
#
# line = file.read(1000)
# file.close()
with open(file_name, mode='r', encoding='cp1251') as file:
    for line in file:
        line = line[:-1]
        list_symbols = []
        for symbol in line:
            if not symbol.isalpha():
                continue
            key = ord(symbol)
            list_symbols.append(key)

            # list_symbols.append(symbol)
        if not list_symbols:
            continue

        list_symbols.sort()

        dict_symbols = Counter(list_symbols)
        dict_symbols_all = {**dict_symbols_old, **dict_symbols}
        dict_symbols_old = dict_symbols_all
        # new = {**old1, **old2}

        # for index, value in enumerate(list_symbols):
        #     if list_symbols[index]== list_symbols[index+1]:
        #         v
        # dict_symbols = {key:  for key in line}
        # value_new =
        # dict_symbols = {key: value_new for key in line}
        print(dict_symbols_old)
        print(dict_symbols)
    print(len(dict_symbols_old))
    print(dict_symbols_old)
# TODO не получается сложить словари - ключи вроде бы добавляет,  а значения не суммирует. есть варианты это исправить?
#
# with open(file_name, mode='r', encoding='cp1251') as file:
#     for line in file:
#         print(line)
#         for symbol in line:
#             if not symbol.isalpha():
#                 continue
#             key = ord(symbol)
#             list_symbols.append(key)  # [ord(symbol) for symbol in line])
#
#         list_symbols.sort()
#         print(list_symbols)
#         for key in list_symbols:
#             value_new =dict_symbols[key] + list_symbols.count(key)
#             print(key, value_new)
#             dict_symbols = {key: value_new for key in list_symbols}
#         print(dict_symbols)
#
#         break
#
# print(line)
print('+----------+-----------+')
print('|  буква   |  частота  |')
print('+----------+-----------+')
# for key in dict_symbols_old:
#     value_dict = dict_symbols_Old[key]
#     print('|   ', key, '    |    ', value_dict, '    |')
#     sum_all_symbol += value_dict

for key in dict_symbols_old:
    value_dict = dict_symbols_old[key]
    print('|   ', chr(key), '    |    ', value_dict, '    |')
    sum_all_symbol += value_dict

print('+----------+-----------+')
print('|  итого   |', sum_all_symbol, ' |')
print('+----------+-----------+')

# берет первый символ в строке, проверяет является ли этот символ буквой, извлекает код символа и создает из него ключ
# значением ключа присваивает 1
# проверяет следующее значение кода символа на наличие в словаре, если имеется заменяет на +1
# если нет. то создается новый ключ -  код символа


# file_content.isalpha()


# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
