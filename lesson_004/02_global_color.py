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


color_draw = 0
color_num = 0

# TODO Используйте Code/Reformat code для внесения правок по стилю

colors = {
    '0': {'color_name': 'red', 'sd_name': sd.COLOR_RED},
    '1': {'color_name': 'orange', 'sd_name': sd.COLOR_ORANGE},
    '2': {'color_name': 'yellow', 'sd_name': sd.COLOR_YELLOW},
    '3': {'color_name': 'cyan', 'sd_name': sd.COLOR_CYAN},
    '4': {'color_name': 'blue', 'sd_name': sd.COLOR_BLUE},
    '5': {'color_name': 'purple', 'sd_name': sd.COLOR_PURPLE},
    '6': {'color_name': 'green', 'sd_name': sd.COLOR_GREEN},
}

# TODO все def надо держать в верхенй части программы, а остальной код после всех def
def color_number():
    color_num = input('Введите желаемый номер цвета:')

    color_digit = color_num

    if not color_digit.isdigit():
        print('вы ввели не число, попробуйте еще раз')
        color_num = 0
        color_number()  # TODO Вместо рекурсий старайтесь использовать циклы там, где это возможно
        # TODO Тут можно просто цикл while использовать, который будет повторять инпут до тех пор
        # TODO пока ввод не будет верным
        # TODO Кроме того два этих условия можно объединить в одно "Если ввод есть в ключах словаря"

    if 0 < int(color_num) > 6:
        print('вы ввели некорректный номер, попробуйте еще раз')
        color_number()

    else:
        return color_num

def n_gon(point, angle=0, length=50, n=3, width=3):
    color_draw = colors[color_num]['sd_name']

    sd.resolution = 1200, 600

    if n < 3:
        print('мало углов')
        return
    i = 0
    angle_n = 360 // n
    point_n = point
    vn = None
    while i < n - 1:
        vn = sd.get_vector(start_point=point_n, angle=angle + angle_n * i, length=length)
        sd.line(start_point=point_n, end_point=vn.end_point, color=color_draw, width=width)

        point_n = vn.end_point
        i += 1

    sd.line(start_point=vn.end_point, end_point=point, color=color_draw, width=width)

    sd.pause()





print('Возможные цвета:')
for number, color_name in colors.items():
    print(number, ':',  colors[number]['color_name'])



color_num = color_number()

point = sd.get_point(600, 250)

n_gon(point, angle=0, length=50, n=12, width=4)
# работает до n = 25, при длине вектора length < 50 дальше накапливается ошибка в углах поворота вектора
