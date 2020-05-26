# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
x = 600
y = 300
radius = 100
color = sd.COLOR_DARK_GREEN
width = 1
count = 0

for _ in range(3):
    point = sd.get_point(x, y)
    sd.circle(center_position=point, radius=radius, color=color, width=width)
    radius -= 5


# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет

def circle_param(x1, y1, radius_circle, color_circle, width_circle):
    for _ in range(3):
        point_1 = sd.get_point(x1, y1)
        sd.circle(center_position=point_1, radius=radius_circle, color=color_circle, width=width_circle)
        radius_circle -= 5


circle_param(300, 300, 150, sd.COLOR_YELLOW, 1)

# Нарисовать 10 пузырьков в ряд
x = 100
y = 100
color = sd.COLOR_DARK_GREEN
width = 1

for x in range(51, 1012, 101):
    circle_param(x, 51, 50, sd.COLOR_YELLOW, 1)

# Нарисовать три ряда по 10 пузырьков
radius = 25
for y in range(550, 400, - 50):
    for x in range(51, 1012, 50):
        circle_param(x, y, radius, sd.COLOR_RED, 1)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
scoring = 100
#
for _ in range(scoring):
    x = sd.random_number(0, 1200)
    y = sd.random_number(0, 600)
    radius = 25
    color = sd.random_color()
    width = 1
    circle_param(x, y, radius, color, width)

sd.pause()
#зачет!