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


x = 0
y = 570
N = 20

n_list_x = []
n_list_x2 = []
n_list_y2 = []
factor_b_list = []

length = 15
step = int(length / 2)

# for i in range(N):
#     x = i * length * 4
#     n_list_x.append(x)
#
#     n_list_x2.append(0)
#     n_list_y2.append(0)
#
#     factor_b_random = sd.random_number(1, 10) / 10
#     factor_b_list.append(factor_b_random)

sd.resolution = 1200, 600

while True:
    # TODO Заполнять снежинки нужно до цикла While
    for i in range(N):
        x = i * length * 4
        n_list_x.append(x)

        n_list_x2.append(0)
        n_list_y2.append(0)

        factor_b_random = sd.random_number(1, 10) / 10
        factor_b_list.append(factor_b_random)
    # TODO Внутри цикла while нужен один цикл по снежинкам, остальное - лищнее
    # TODO Лучшей практикой будет for i, y in enumerate(список):
    # TODO Так у вас будет доступ и к индексам (i) и к объектам списка
    # TODO В итоге алгоритм следующий
    # TODO цикл while:
    # TODO   циклом проходим по списку со снежинками
    # TODO     получаем точку из текущих координат
    # TODO     рисуем снежинку фоном
    # TODO     меняем координату и получаем новую точку
    # TODO     рисуем снежинку белым цветом
    # TODO Про то, что делать с упавшими снежинками поговорим после реализации этой части алгоритма
    for y in range(570, 0, - step):

        for i in range(N):
            x1 = n_list_x2[i]
            y1 = n_list_y2[i]

            point = sd.get_point(x1, y1)

            factor_b = factor_b_list[i]

            sd.start_drawing()

            sd.snowflake(center=point, length=length, color=sd.background_color, factor_b=factor_b)

        for i in range(N):
            x1 = n_list_x[i] + sd.random_number(0, 25)
            y1 = y + sd.random_number(0, 15)

            n_list_x2[i] = x1

            n_list_y2[i] = y1

            point = sd.get_point(x1, y1)

            factor_b = factor_b_list[i]

            sd.snowflake(center=point, length=length, color=sd.COLOR_WHITE, factor_b=factor_b)

            sd.finish_drawing()

        #sd.sleep(0.2) # чтобы быстрее проходил цикл - поставил диез

        if y <= length:
            for i in range(N):
                x1 = n_list_x2[i]
                y1 = n_list_y2[i]

                point = sd.get_point(x1, y1)

                factor_b = factor_b_list[i]

                sd.snowflake(center=point, length=length, color=sd.background_color, factor_b=factor_b)

            for i in range(N):
                x1 = n_list_x2[i]
                y1 = 0

                point = sd.get_point(x1, y1)

                factor_b = factor_b_list[i]

                sd.snowflake(center=point, length=length, color=sd.COLOR_WHITE, factor_b=factor_b)

    factor_b_list = []

    if sd.user_want_exit():
        break

sd.pause()
