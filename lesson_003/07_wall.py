# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
sd.resolution = (600, 600)

for row, y in enumerate(range(0, 600, 50)):
    x0 = -50 if row % 2 == 0 else 0
    for x in range(x0, 600, 100):
        left_bottom = sd.get_point(x, y)
        right_top = sd.get_point(x + 100, y + 50)
        sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_YELLOW, width=1)

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
#зачет!