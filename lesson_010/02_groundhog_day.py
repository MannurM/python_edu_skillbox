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


def one_day():
    # TODO отсюда цикл можно убрать
    while ENLIGHTENMENT_CARMA_LEVEL >= 7:
        random_exception = randint(1, 13)

        if random_exception == 7:
            # TODO наоборот, если выпадает 7, то карму возвращать не нужно
            # TODO тут надо вызвать случайное исключение
            carma_level = randint(1, 7)
            # print(carma_level, 'carma_level')
            # TODO кстати исключения можно собрать в список или словарь и вызывать их оттуда по индексу/ключу
            if carma_level == 1:
                raise IamGodError('IamGodError')
            elif carma_level == 2:
                raise DrunkError('DrunkError')
            elif carma_level == 3:
                raise CarCrashError('CarCrashError')
            elif carma_level == 4:
                raise GluttonyError('GluttonyError')
            elif carma_level == 5:
                raise GluttonyError('GluttonyError')
            elif carma_level == 6:
                raise SuicideError('SuicideError')
            else:
                print('Good day!')
            return carma_level
        # TODO тут нужен else и в нём возвращать карму от 1 до 7

# TODO тут нужна будет переменная для хранения кармы
# TODO чтобы было while результат <= ENLIGHTENMENT_CARMA_LEVEL
while ENLIGHTENMENT_CARMA_LEVEL >= 7:
    try:
        one_day()

    # TODO Тут нужно будет перечислить все типы ошибок в except
    # TODO Их можно объединять подобным образом
    #  except (ValueError, Exception ...) as exc
    except IamGodError as exc:
        print(f' ошибка  - {exc}')
    except DrunkError as exc:
        print(f' ошибка  - {exc}')
    except CarCrashError as exc:
        print(f' ошибка  - {exc}')
    except GluttonyError as exc:
        print(f' ошибка  - {exc}')
    except DepressionError as exc:
        print(f' ошибка  - {exc}')
    except SuicideError as exc:
        print(f' ошибка  - {exc}')
    # except:
    #     print('Другая ошибка!')

# https://goo.gl/JnsDqu
