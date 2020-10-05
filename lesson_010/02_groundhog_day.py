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

# TODO хранить стоит объекты класса, а не классы, + им можно передавать уточняющие сообщения
dict_exception = {1: IamGodError, 2: DrunkError, 3: CarCrashError, 4: GluttonyError, 5: SuicideError, 6: SuicideError, }
carma_level = 0


def one_day():
    global carma_level
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
        carma_level += carma  # TODO кармы надо возвращать от 1 до 7
        return carma_level


while ENLIGHTENMENT_CARMA_LEVEL >= carma_level:
    try:
        one_day()

    # except IamGodError as exc1:
    #     print('ошибка1 - ', exc1)
    # except DrunkError as exc2:
    #     print('ошибка2 - ', exc2)
    # except CarCrashError as exc3:
    #     print('ошибка3 - ', exc3)
    # except GluttonyError as exc4:
    #     print('ошибка4 - ', exc4)
    # except DepressionError as exc5:
    #     print('ошибка5 - ', exc5)
    # except SuicideError as exc6:
    #     print('ошибка6 - ', exc6)
    except (IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError) as exc:
        print(f' ошибка  - {repr(exc)}')  # что - то не так  - не выводит вид ошибки
        # TODO можно использовать функцию repr()
        # TODO только запись надо вести в файл
print('Congratulations! A new day has come!')

# https://goo.gl/JnsDqu
