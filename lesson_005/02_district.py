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

# print('На районе живут: ', end='')

from district.central_street.house1.room1 import folks as folks1
from district.central_street.house1.room2 import folks as folks2
from district.central_street.house2.room1 import folks as folks3
from district.central_street.house2.room2 import folks as folks4
from district.soviet_street.house1.room1 import folks as folks5
from district.soviet_street.house1.room2 import folks as folks6
from district.soviet_street.house2.room1 import folks as folks7
from district.soviet_street.house2.room2 import folks as folks8

folks_cs = folks1 + folks2 + folks3 + folks4  # с центральной улицы
folks_ss = folks5 + folks6 + folks7 + folks8  # с советской улицы

folks = folks_cs + folks_ss
print(', '.join(folks))
#зачет!