# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
from random import randint

ENLIGHTENMENT_CARMA_LEVEL = 777
carma_error_list = []


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


iamgod = IamGodError()
drunk = DrunkError()
carcrash = CarCrashError()
gluttony = GluttonyError()
suicide = SuicideError()
depression = DepressionError()

dict_exception = {1: iamgod, 2: drunk, 3: carcrash, 4: gluttony, 5: depression, 6: suicide}
carma_level = 0


def one_day():
    carma = randint(1, 13)
    if carma == 7:
        random_exp = randint(1, 6)
        raise dict_exception[random_exp]
    else:
        return carma


while ENLIGHTENMENT_CARMA_LEVEL >= carma_level:
    try:
        carma_level += one_day()
    except (IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError) as exc:
        carma_error_list.append(repr(exc))
        carma_level -= 7  # карма должна уменьшаться за плохие поступки))

file_name = 'carma_error.log'
file = open(file_name, mode='w')
for line in carma_error_list:
    line = str(line) + '\n'
    file.write(line)
file.close()

print('Congratulations! A new day has come!')

# https://goo.gl/JnsDqu
#зачёт!