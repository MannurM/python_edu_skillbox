# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

color_draw = 0
color_num = 0
n_gon_in = 0
colors = {
    0: sd.COLOR_RED,
    1: sd.COLOR_ORANGE,
    2: sd.COLOR_YELLOW,
    3: sd.COLOR_GREEN,
    4: sd.COLOR_CYAN,
    5: sd.COLOR_BLUE,
    6: sd.COLOR_PURPLE,
}


def n_gon(point, angle=0, length=50, n=3, width=3):
    color_draw = colors.get(int(color_num))

    sd.resolution = 1200, 600

    if n < 3:
        print('мало углов')
        return
    i = 0
    angle_n = 180 - (n - 2) * 180 / n
    point_n = point

    while i < n - 1:
        vn = sd.get_vector(start_point=point_n, angle=angle + angle_n * i, length=length)
        sd.line(start_point=point_n, end_point=vn.end_point, color=color_draw, width=width)

        point_n = vn.end_point
        i += 1

    sd.line(start_point=vn.end_point, end_point=point, color=color_draw, width=width)




def color_number():
    print('Возможные цвета:')
    print('0: red')
    print('1: orange')
    print('2: yellow')
    print('3: green')
    print('4: cyan')
    print('5: blue')
    print('6: purple')

    color_num = input('Введите желаемый номер цвета:')

    color_digit = color_num

    if not color_digit.isdigit():
        print('вы ввели не число, попробуйте еще раз')
        color_num = 0
        color_number()

    if 0 < int(color_num) > 6:
        print('вы ввели некорректный номер, попробуйте еще раз')
        color_number()

    else:
        return color_num

def n_gon_input():
    print('3')
    print('4')
    print('5')
    print('6')
    print('7')
    print('8')

    n_gon_in = input('Введите желаемое количество углов у фигуры:')

    color_digit = n_gon_in

    if not color_digit.isdigit():
        print('вы ввели не число, попробуйте еще раз')

        n_gon_in = 0

        n_gon_input()

    if 2 <= int(n_gon_in) >= 9:
        print('вы ввели некорректный номер, попробуйте еще раз')

        n_gon_input()

    else:
        return n_gon_in

color_num = 0 # выбор цвета фигур

n = 0

i = 3

for x in range(150, 900, 300):
    for y in range(100, 600, 300):
        n = i

        n_gon(point=sd.get_point(x, y), angle=0, length=50, n=n, width=4)

        i += 1

print("Рисуем Вашу фигуру")

color_num = color_number()# выбор цвета

n_gon_in = int(n_gon_input())# выбираем количество углов

x = 600
y = 200


sd.clear_screen()

n_gon(point=sd.get_point(x, y), angle=0, length=100, n=n_gon_in, width=5)

sd.pause()



