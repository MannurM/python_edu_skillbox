 # -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
root_point = sd.get_point(600, 30)
#

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения
sd.resolution = 1200, 700

start_point = 0

# def draw_branches(start_point=start_point, angle=90, length=100, width=1):
#     trunk = sd.get_vector(start_point=root_point, angle=angle, length=100, width=1)
#     trunk.draw()
#
#     brunch_1 = sd.get_vector(start_point=trunk.end_point, angle=angle-30, length=100, width=1)
#     brunch_1.draw()
#
#     brunch_2 = sd.get_vector(start_point=trunk.end_point, angle=angle + 30, length=100, width=1)
#     brunch_2.draw()

# def branch(point, angle, length, delta):
#     if length < 1:
#         return
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#     next_point = v1.end_point
#     next_angle = angle - delta
#     next_length = length * .75
#     branch(point=next_point, angle=next_angle, length=next_length, delta=delta)


# def draw_branches(start_point, angle=90, length=50, width=1):
#
#
#
#     trunk = sd.get_vector(start_point=start_point, angle=angle, length=length, width=1)
#     trunk.draw()
#
#     if length < 1:
#         return
#
#     brunch_1 = sd.get_vector(start_point=trunk.end_point, angle=angle-30, length=length, width=1)
#     brunch_1.draw()
#
#     brunch_2 = sd.get_vector(start_point=trunk.end_point, angle=angle + 30, length=length, width=1)
#     brunch_2.draw(color=sd.COLOR_DARK_YELLOW)
#
#     next_angle = angle - 30
#
#     next_point_1 = brunch_1.end_point
#     next_length_1 = length * .75
#
#     next_point_2 = brunch_2.end_point
#     next_length_2 = length * .75
#
#     draw_branches(start_point=next_point_1, angle=next_angle, length=next_length_1,)
#
#     draw_branches(start_point=next_point_2, angle=next_angle+60, length=next_length_2,)
#
# draw_branches(start_point=root_point, angle=90, length=100)



# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()
sd.resolution = 600, 600
root_point = sd.get_point(300, 30)
# TODO Используйте Code/Reformat code для внесения правок по стилю
def draw_branches(start_point, angle=90, length=75, width=1):

    trunk = sd.get_vector(start_point=start_point, angle=angle, length=length, width=1)
    trunk.draw()

    if length < 1:
        return
    # TODO Тут не нужно два вектора рисовать, достаточно одного
    # TODO А тк в функции вызывается два раза эта же функция, то и будут нарисованы две ветки
    # TODO рисуем вектор с текущими параметрами, затем рассчитать новые параметры и передать их в вызовы
    brunch_1 = sd.get_vector(start_point=trunk.end_point, angle=angle-30, length=length, width=1)
    brunch_1.draw()

    brunch_2 = sd.get_vector(start_point=trunk.end_point, angle=angle + 30, length=length, width=1)
    brunch_2.draw(color=sd.COLOR_DARK_YELLOW)

    random_angle = sd.random_number(1, 40)/100
    random_length = sd.random_number(1, 20)/100 * .75


    next_angle = angle - 30 * random_angle

    next_point_1 = brunch_1.end_point
    next_length_1 = length * (.75 - random_length)

    next_point_2 = brunch_2.end_point
    next_length_2 = length * (.75 - random_length)

    draw_branches(start_point=next_point_1, angle=next_angle, length=next_length_1,)

    draw_branches(start_point=next_point_2, angle=next_angle+60*random_angle, length=next_length_2,)

draw_branches(start_point=root_point, angle=90, length=100)




sd.pause()


