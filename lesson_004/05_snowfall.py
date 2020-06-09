# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные
# x = 0
# y = 570
# N = 20
#
# n_list_x = []
# factor_b_list = []
#
# length = 15
# step = int(length / 2)
#
#
# for i in range(N):
#     x = i * length * 4
#     n_list_x.append(x)
#
#     factor_b_random = sd.random_number(1, 10)/10
#     factor_b_list.append(factor_b_random)
#
#
# sd.resolution = 1200, 600
#
# for y in range(570, length, - step):
#
#     for i in range(N):
#         point = sd.get_point(n_list_x[i]+sd.random_number(0, 20), y + sd.random_number(0, 25))
#
#         factor_b = factor_b_list[i]
#
#         sd.snowflake(center=point, length=length, factor_b=factor_b)
#
#     sd.sleep(0.1)
#
#     sd.clear_screen()
#
#     if sd.user_want_exit():
#         break


# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


# Примерный алгоритм отрисовки снежинок
#   навсегда
#     очистка экрана
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       создать точку отрисовки снежинки
#       нарисовать снежинку цветом фона
#       изменить координата_у и запомнить её в списке по индексу
#       создать новую точку отрисовки снежинки
#       нарисовать снежинку на новом месте белым цветом
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# Часть 2 (делается после зачета первой части)
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла
# - в начале рисования всех снежинок вызвать sd.start_drawing()
# - на старом месте снежинки отрисовать её же, но цветом sd.background_color
# - сдвинуть снежинку
# - отрисовать её цветом sd.COLOR_WHITE на новом месте
# - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()

# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


def snow():
    N = 20  # количество снежинок 1200/N
    length = 15
    count = 0
    step_drift = length
    step_count = 250

    n_list_x1 = []
    n_list_y1 = []

    factor_a_list = []
    factor_b_list = []
    step_random_x = []
    step_random_y = []

    sd.resolution = 1200, 600

    for i in range(int(1200 / N)):
        x = sd.random_number(- length, 1200)
        n_list_x1.append(x)

        factor_a_random = sd.random_number(3, 9) / 10
        factor_a_list.append(factor_a_random)

        factor_b_random = sd.random_number(1, 15) / 10
        factor_b_list.append(factor_b_random)

        step_x = sd.random_number(-10, 10)
        step_random_x.append(step_x)

        step_y = sd.random_number(5, 25)
        step_random_y.append(step_y)

        y = 750
        n_list_y1.append(y)

    while True:
        count += 1
        sd.start_drawing()

        for i, x in enumerate(n_list_x1):
            factor_a = factor_a_list[i]
            factor_b = factor_b_list[i]
            x = n_list_x1[i]
            y = n_list_y1[i]

            point = sd.get_point(x, y)

            sd.snowflake(center=point, length=length, color=sd.background_color, factor_a=factor_a, factor_b=factor_b)

            n_list_x1[i] = x = n_list_x1[i] + step_random_x[i]
            n_list_y1[i] = y = n_list_y1[i] - step_random_y[i]

            point = sd.get_point(x, y)

            sd.snowflake(center=point, length=length, color=sd.COLOR_WHITE, factor_a=factor_a, factor_b=factor_b)

            if count == step_count:
                step_drift += length
                step_count += 200

            if y <= step_drift:
                n_list_y1[i] = 650
                n_list_x1[i] = sd.random_number(-4 * length, 1300)

        if y == 649:  # TODO Вот только это условие непонятное осталось, остальное выполнено верно
            break

        sd.finish_drawing()
        sd.sleep(0.09)

        if sd.user_want_exit():
            break


snow()
sd.pause()
