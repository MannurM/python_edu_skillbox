# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

# from package_1 import module_1
# module_1.function1()
#
# from package_1.module_1 import function1
# function1()
#
# import package_1.module_1
# package_1.module_1.function1()  # тут нужно полное имя модуля
#
# # подпакеты
# from package_1.subpackage import module_2
# module_2.function2()
#
# from package_1.subpackage.module_2 import function2
# function2()
#
# import package_1.subpackage.module_2
# package_1.subpackage.module_2.function2()
#
# import package_1
# package_1.subpackage.module_2.function2()
#
# from package_1.subpackage import module_2
# module_2.function2()

print('На районе живут: ', end='')  # TODO Все импорты надо перенести в самый верх
# TODO Списка названть по разному (можно добавлять к названию номера домов и комнат)
# TODO Списки после импорта сложить (через +) и применить один Join

from district.central_street.house1.room1 import folks

print(', '.join(folks))

from district.central_street.house1.room2 import folks

print(', '.join(folks))

from district.central_street.house2.room1 import folks

print(', '.join(folks))

from district.central_street.house2.room2 import folks

print(', '.join(folks))

from district.soviet_street.house1.room1 import folks

print(', '.join(folks))

from district.soviet_street.house1.room2 import folks

print(', '.join(folks))

from district.soviet_street.house2.room1 import folks

print(', '.join(folks))

from district.soviet_street.house2.room2 import folks

print(', '.join(folks))

# TODO А можно ли перебрать весь пакет 'district' через вложенные циклы?