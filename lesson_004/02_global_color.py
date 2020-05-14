# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

sd.resolution = 1200, 600


def n_gon(point, angle=0, length=100, color, n=3):
    if n < 3:
        print('мало углов')
        return
    i = 0
    angle_n = 180 - (n - 2) * 180 / n
    point_n = point

    while i < n - 1:
        vn = sd.get_vector(start_point=point_n, angle=angle + angle_n * i, length=length, color=color, width=3)
        vn.draw()

        point_n = vn.end_point
        i += 1

    sd.line(start_point=vn.end_point, end_point=point, width=3)


point = sd.get_point(600, 250)

n_gon( angle=0, n=14, length=50)# работает до n = 25, при длине вектора length < 50 дальше накапливается ошибка в углах поворота вектора


sd.pause()
