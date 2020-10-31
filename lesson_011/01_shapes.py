# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def poly_gon(n):
    angle_step = 360 // n
    length = 100
    point = sd.get_point(300, 300)
    point_n = point
    start_angle = 90
    vn = None
    for angle in range(0, 360 - angle_step, angle_step):
        vn = sd.get_vector(start_point=point_n, angle=start_angle + angle, length=length, width=3)
        vn.draw()
        point_n = vn.end_point
    sd.line(start_point=vn.end_point, end_point=point, width=3)


poly_gon(n=3)
poly_gon(n=4)
poly_gon(n=5)
poly_gon(n=6)


sd.pause()
