# -*- coding: utf-8 -*-

# Вас взяли на работу в молодой стартап. Идея стартапа - предоставлять сервис расчета результатов игр.
# Начать решили с боулинга, упрощенной версии.
#
# Правила такие.
#
# Всего 10 кеглей. Игра состоит из 10 фреймов. В одном фрейме до 2х бросков, цель - сбить все кегли.
# Результаты фрейма записываются символами:
#   «Х» – «strike», все 10 кеглей сбиты первым броском
#   «<число>/», например «4/» - «spare», в первый бросок сбиты 4 кегли, во второй – остальные
#   «<число><число>», например, «34» – в первый бросок сбито 3, во второй – 4 кегли.
#   вместо <число> может стоять прочерк «-», например «-4» - ни одной кегли не было сбито за первый бросок
# Результат игры – строка с записью результатов фреймов. Символов-разделителей между фреймами нет.
# Например, для игры из 4 фреймов запись результатов может выглядеть так:
#   «Х4/34-4»
# Предлагается упрощенный способ подсчета количества очков:
#   «Х» – strike всегда 20 очков
#   «4/» - spare всегда 15 очков
#   «34» – сумма 3+4=7
#   «-4» - сумма 0+4=4
# То есть для игры «Х4/34-4» сумма очков равна 20+15+7+4=46
#
# Надо написать python-модуль (назвать bowling), предоставляющий API расчета количества очков:
# функцию get_score, принимающую параметр game_result. Функция должна выбрасывать исключения,
# когда game_result содержит некорректные данные. Использовать стандартные исключения по максимуму,
# если не хватает - создать свои.
#
# Обязательно написать тесты на этот модуль. Расположить в папке tests.

# Из текущего файла сделать консольную утилиту для определения количества очков, с помощью пакета argparse
# Скрипт должен принимать параметр --result и печатать на консоль:
#   Количество очков для результатов ХХХ - УУУ.


import argparse
import bowling


def create_parser():
    parser = argparse.ArgumentParser(description='bowling')
    parser.add_argument('--result', type=str, required=True, help='data_Bowling')
    return parser


# if __name__ == '__main__':
#     parser = create_parser()
#     args = parser.parse_args('--result X2/-353XX9/-7-523'.split())
#     # args = parser.parse_args()
#     # res = bowling.get_score(game_result=args.result)
#     res_one = bowling.CounterBowling(game_result=args)
#     res = res_one.get_store(game_result=args.result)
#     print(f'Количество очков - {res}!')

if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args('--result X2/-353XX9/0055'.split())
    # args = parser.parse_args('--result X2/-353XX9/--45'.split())
    #  в текущем фрейме 3 ошибки
    # 1) длина меньше 10 (должна быть ровно 10 фреймов)
    # 2) есть нули 00 (должны быть --, нули должны вызывать ошибку)
    # 3) сумма цифр во фреме больше 9 (55 - 5+5=10, по сути тут должен был быть 5/)
    # каждая из этих ошибок должны вызывать исключение
    # args = parser.parse_args()
    # res = bowling.get_score(game_result=args.result)
    res_one = bowling.Game(game_result=args)
    res = res_one.run_game(game_result=args.result)
    print(f'Количество очков - {res}!')


# При написании кода помнить, что заказчик может захотеть доработок и новых возможностей...
# И, возможно, вам пригодится паттерн проектирования "Состояние",
#   см https://clck.ru/Fudd8 и https://refactoring.guru/ru/design-patterns/state
