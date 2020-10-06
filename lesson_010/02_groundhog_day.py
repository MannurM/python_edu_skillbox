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
carma = 0


def one_day():
    global carma_level, carma  # TODO глобалы использовать стоит в редких случаях
    # TODO идея то хорошая, я её понял и реализация верная, но очень советую избавляться от привычки
    # TODO использовать глобалы
    carma = randint(1, 13)
    if carma == 7:
        random_exp = randint(1, 6)
        print('Bad Day!')
        print(carma_level, 'carma_level')
        carma_level -= random_exp  # карма должна уменьшаться за плохие поступки))
        raise dict_exception[random_exp]
    else:
        # print('Good day!')
        # print(carma_level, 'carma_level')
        return carma_level


file_name = 'carma_error.log'

while ENLIGHTENMENT_CARMA_LEVEL >= carma_level:
    try:
        one_day()
        carma_level += carma
    except (IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError) as exc:
        # TODO открывать файл в цикле не стоит, это будет добавлять много лишних тяжелых действий пайтону
        with open(file_name, mode='a') as file:
            file.write(repr(exc))


print('Congratulations! A new day has come!')

# https://goo.gl/JnsDqu
