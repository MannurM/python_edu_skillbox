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
x1 = 0
y = 0
y1 = 0
N = 20
length = 15

n_list_x = []
n_list_x1 = [0]
n_list_y = []
factor_b_list = [0]
step_random_x = []
step_random_y = [0]

sd.resolution = 1200, 600

n_list_y = [y for y in range(600, 0, int(-length / 2))]
print(n_list_y)
for i in range(N):
    x = i * length * 4
    n_list_x.append(x)

    factor_b_random = sd.random_number(1, 10) / 10
    factor_b_list.append(factor_b_random)

    step_x = sd.random_number(1, 30)
    step_random_x.append(step_x)

    step_y = sd.random_number(1, 15)
    step_random_y.append(step_y)
print(step_random_y)
print(step_random_x)
# sd.start_drawing()

while True:
    # TODO Так у вас будет доступ и к индексам (i) и к объектам списка
    # TODO В итоге алгоритм следующий
    # TODO цикл while:
    # TODO   циклом проходим по списку со снежинками
    # TODO     получаем точку из текущих координат
    # TODO     рисуем снежинку фоном
    # TODO     меняем координату и получаем новую точку
    # TODO     рисуем снежинку белым цветом
    # TODO Про то, что делать с упавшими снежинками поговорим после реализации этой части алгоритма

    y = n_list_y[0]

    y1 = n_list_y[1]

    del n_list_y[0]

    # print(y1)
    # print(y)
    for i, x in enumerate(n_list_x):
        factor_b = factor_b_list[i]

        x = n_list_x1[0]
        n_list_x1[0] = 0
        point = sd.get_point(x, y - step_random_y[i])

        sd.snowflake(center=point, length=length, color=sd.background_color, factor_b=factor_b)
        x1 = n_list_x[i] + step_random_x[i]
        print('x', x, 'x1', x1)
        n_list_x1[0] = x1

        point = sd.get_point(x1, y1 - step_random_y[i + 1])
        sd.snowflake(center=point, length=length, color=sd.COLOR_WHITE, factor_b=factor_b)

    sd.sleep(0.05)
    if y <= length:
        break

    if sd.user_want_exit():
        break
# sd.finish_drawing()
sd.pause()
