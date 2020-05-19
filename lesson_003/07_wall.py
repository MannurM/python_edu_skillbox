# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
sd.resolution = (600, 600)


for _ in range(5):
    y = - 99

    for _ in range(6):
        x = - 49
        y += 100

        for _ in range(6):
            x += 100
            left_bottom = sd.get_point(x, y)
            right_top = sd.get_point(x + 100, y + 50)
            left_bottom_2 = sd.get_point(x - 50, y + 50)
            right_top_2 = sd.get_point(x + 50, y + 100)
            sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_YELLOW, width=1)
            sd.rectangle(left_bottom=left_bottom_2, right_top=right_top_2, color=sd.COLOR_YELLOW, width=1)

# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

sd.pause()
