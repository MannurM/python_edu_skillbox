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

def circle_param(x, y, radius, color, width):
    for _ in range(3):
        point = sd.get_point(x, y)
        sd.circle(center_position=point, radius=radius, color=color, width=width)
        radius -= 5



circle_param(300, 300, 150, sd.COLOR_YELLOW, 1)

# Нарисовать 10 пузырьков в ряд
x = 100
y = 100
color = sd.COLOR_DARK_GREEN
width = 1

for i in range(10):
    count = 0
    x = 100 * (i + 1)
    point = sd.get_point(x, y)
    radius = 50

    while count < 3:
        sd.circle(center_position=point, radius=radius, color=color, width=width)
        radius -= 5
        count += 1

# Нарисовать три ряда по 10 пузырьков
x = 50
y = 650
color = sd.COLOR_RED
width = 1

for j in range(3):
    y = y-100

    for i in range(10):
        count = 0
        x = 100 * (i + 1)
        point = sd.get_point(x, y)
        radius = 50

        for _ in range(3):
            sd.circle(center_position=point, radius=radius, color=color, width=width)
            radius -= 5


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
scoring = 0
#
for _ in range(100):
    point = sd.random_point()
    radius = 25
    color = sd.random_color()
    width = 1

    for _ in range(3):
        sd.circle(center_position=point, radius=radius, color=color, width=width)
        radius -= 3



sd.pause()
