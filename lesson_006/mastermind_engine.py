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


# global guess_number_1, guess_number_2, guess_number_3, guess_number_4  TODO Эта строка тут и правда не нужна
# TODO Но саму переменную задать нужно
# TODO число_компьютера = None
# TODO например, просто чтобы создать эту переменную, а в функции уже её заполнять


def make_number():
    global guess_number_1, guess_number_2, guess_number_3, guess_number_4
    # TODO Зачем 4 номера? Нужен 1
    # TODO Тут ещё нужно будет очищать список перед заполнением (для повторых вызовов функций)
    number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # TODO Попробуйте использовать цикл, добавляя по одному числу, пока не будет добавлено 4 числа
    # TODO И в цикле проверять - если число есть в списке - не добавлять, если нету - добавлять
    guess_number_1 = random.choice(number_list[1:])
    number_list.remove(guess_number_1)

    guess_number_2 = random.choice(number_list)
    number_list.remove(guess_number_2)

    guess_number_3 = random.choice(number_list)
    number_list.remove(guess_number_3)

    guess_number_4 = random.choice(number_list)
    number_list.remove(guess_number_4)

    guess_number[0] = str(guess_number_1)
    guess_number[1] = str(guess_number_2)
    guess_number[2] = str(guess_number_3)
    guess_number[3] = str(guess_number_4)

    print(guess_number.values())
    return guess_number


def check_input():
    global count  # TODO глобал должен идти первой строчкой (я уже перенес её выше)
    check_number = '0'
    count = 1
    # TODO Вся эта часть тут не нужна, её надо реализовать в основном модуле.
    # TODO Здесь оставить только проверку числа на быков и коров и возврат быков и коров, без лишних принтов и тд
    while not check_number == guess_number:
        print('Ход', count)
        check_number = input('Введите ваше число:')

        n_digit = check_number
        if not n_digit.isdigit():
            print('вы ввели не число', check_number, ',', 'попробуйте еще раз')
            continue

        if int(check_number) < 1023 or int(check_number) > 9876:
            print('вы ввели некорректное число', check_number, ',', 'попробуйте еще раз')
            continue
        check_number_1 = check_number[0]
        check_number_2 = check_number[1]
        check_number_3 = check_number[2]
        check_number_4 = check_number[3]
        # TODO Для проверки повторов можно использовать set()
        # TODO Если из списка чисел сделать множество при помощи set()
        # TODO то из него удалятся все дубли.
        if check_number_1 == check_number_2 or check_number_1 == check_number_3 or check_number_1 == check_number_4:
            print('невозможно проверить, в вашем числе повторяющиеся цифры. ', check_number)
            continue
        elif check_number_2 == check_number_3 or check_number_2 == check_number_4:
            print('невозможно проверить, в вашем числе повторяющиеся цифры. ', check_number)
            continue
        elif check_number_3 == check_number_4:
            print('невозможно проверить, в вашем числе повторяющиеся цифры. ', check_number)
            continue

        # if check_number_1 == guess_number_1 and check_number_2 == guess_number_2 and check_number_3 == guess_number_3 and check_number_4 == guess_number_4:
        #     return print('число угадано!!!')
        # else:
        bull, cow = 0, 0

        for key, value in guess_number.items():

            if check_number[key] == guess_number[key]:
                bull += 1
                cow += 1
            elif check_number[key] in guess_number.values():
                cow += 1
        # TODO Печатать тут ничего не нужно, просто возвращайте быков и коров
        # TODO А уже результат считать и печатать нужно там, в 01
        print('cows -', cow, 'цифры есть в числе')
        print('bulls -', bull, 'цифры на своем месте')
        print(' ')
        count += 1
        if bull == 4 and cow == 4:
            print('число угадано!!!')
            return count


count = 1
guess_number = {}
