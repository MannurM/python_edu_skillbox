# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = 1200, 600


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Примерный алгоритм внутри функции:
#   # будем рисовать с помощью векторов, каждый следующий - из конечной точки предыдущего
#   текущая_точка = начальная точка
#   для угол_наклона из диапазона от 0 до 360 с шагом XXX
#      # XXX подбирается индивидуально для каждой фигуры
#      составляем вектор из текущая_точка заданной длины с наклоном в угол_наклона
#      рисуем вектор
#      текущая_точка = конечной точке вектора
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# def triangle(point, angle=0, length=100):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
#     v3.draw()
#
#
# def square(point, angle=0, length=100):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=3)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length, width=3)
#     v3.draw()
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=length, width=3)
#     v4.draw()
#
#
# def pentagon(point, angle=0, length=100):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=3)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, width=3)
#     v3.draw()
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length, width=3)
#     v4.draw()
#
#     v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 288, length=length, width=3)
#     v5.draw()
#
#
# def hexagon(point, angle=0, length=100):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=3)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=3)
#     v3.draw()
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=3)
#     v4.draw()
#
#     v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length, width=3)
#     v5.draw()
#
#     v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 300, length=length, width=3)
#     v6.draw()
#
#
# point = sd.get_point(1, 1)
# triangle(point, length=200, angle=30)
#
# point = sd.get_point(240, 1)
# square(point, length=200, angle=30)
#
# point = sd.get_point(550, 1)
# pentagon(point, length=200, angle=30)
#
# point = sd.get_point(970, 1)
# hexagon(point, angle=30)


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.
# TODO Используйте Code/Reformat code для внесения правок по стилю
# Часть 2 (делается после зачета первой части) - Эх, устал ждать когда проверят третий урок - сделал вот такую функцию.
angle_n = []  # TODO В данном случае этот список не нужен, но на будущее - его стоило расположить внутри функции
def n_gon(point, angle, length=100, n=3):  # TODO Стоит ещё подумать над названием
    if n < 3:
        print('мало углов')
        return
    i = 0
    # angle_n = 360 // n  # TODO Это хорошая идея, чтобы использовать дальше переменную, вместо рассчётов заново
    # TODO правда назвать стоило бы angle_step например
    point_n = point
    vn = None
    angle_original = angle
    for angle in range(0, 360 - (360//n), 360//n):
        angle_n.append(angle + angle_original)
        # print(angle_n)
    # for angle in range(0, 360 - (360 // n), 360 // n):
    while i < n - 1:  # TODO Второй цикл не нужен, векторы можно нарисовать в первом, там
        # TODO где рассчитываются сами углы
        # print(angle_n[i])
        vn = sd.get_vector(start_point=point_n, angle=angle_n[i], length=length, width=3)
        vn.draw()
        point_n = vn.end_point
        i += 1

    sd.line(start_point=vn.end_point, end_point=point, width=3)
    angle_n.clear()
    # print(angle_n)


def triangle(point, angle=0, length=100):  # TODO Тут вы уже получаете точку point снаружи
    point = sd.get_point(300, 50)  # TODO не нужно создавать новую
    n_gon(point, angle, length, n=3)

def square(point, angle=0, length=100):
    point = sd.get_point(300, 250)
    n_gon(point, angle, length, n=4)

def pentagon(point, angle=0, length=100):
    point = sd.get_point(900, 50)
    n_gon(point, angle, length, n=5)

def hexagon(point, angle=0, length=100, n=6):
    point = sd.get_point(900, 250)
    n_gon(point, angle, length, n=6)


triangle(point=0, angle=30, length=50)
square(point=0, angle=50, length=100)
pentagon(point=0, angle=-15, length=70)
hexagon(point=0, angle=0, length=120)

# n_gon(point, angle=0, n=14, length=50)
# работает до n = 25, при длине вектора length < 50 дальше накапливается ошибка в углах поворота вектора
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
