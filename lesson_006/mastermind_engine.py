# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В mastermind_engine нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
#
# В текущем модуле (lesson_006/01_mastermind.py) реализовать логику работы с пользователем:
#   модуль движка загадывает число
#   в цикле, пока число не отгадано
#       у пользователя запрашивается вариант числа
#       проверяем что пользователь ввел допустимое число (4 цифры, все цифры разные, не начинается с 0)
#       модуль движка проверяет число и выдает быков/коров
#       результат быков/коров выводится на консоль
#  когда игрок угадал таки число - показать количество ходов и вопрос "Хотите еще партию?"
#
# При написании кода учитывайте, что движок игры никак не должен взаимодействовать с пользователем.
# Все общение с пользователем (вывод на консоль и запрос ввода от пользователя) делать в 01_mastermind.py.
# Движок игры реализует только саму функциональность игры. Разделяем: mastermind_engine работает
# только с загаданным числом, а 01_mastermind - с пользователем и просто передает числа на проверку движку.
# Это пример применения SOLID принципа (см https://goo.gl/GFMoaI) в архитектуре программ.
# Точнее, в этом случае важен принцип единственной ответственности - https://goo.gl/rYb3hT
import random

guess_number = None  # сперва глобальную переменную надо обозначить, а затем уже на неё ссылаться в функциях


def make_number():
    global guess_number
    guess_number = None
    number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    guess_number_list = []
    count_make_number = 0
    while count_make_number <= 3:
        guess_number_make = random.choice(number_list)

        if count_make_number == 0 and guess_number_make == '0':
            continue
        if guess_number_make in guess_number_list:
            continue
        else:
            guess_number_list.append(guess_number_make)
            count_make_number += 1

    guess_number = ''.join(guess_number_list)
    print(guess_number)
    return guess_number


def check_bull_cow(check_number):
    global guess_number
    bull, cow = 0, 0
    for key, value in enumerate(guess_number):
        if check_number[key] == guess_number[key]:
            bull += 1
        elif check_number[key] in guess_number:
            cow += 1
    return cow, bull
